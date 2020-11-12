from operator import add, sub

def connector(name=None):
    """A connector between constraints."""
    informant = None # current value's source
    constraints = [] # an array of constraints where the connector is involved in
    
    # records the source(which might be a constraint or user) of the value so that later on we inform all constraints but not the source (inform_all_except at the end of the function body) to avoid repetition
    def set_value(source, value):
        # informant will always be either a single value recording the source of the current value of the connector or None
        nonlocal informant
        # fetch the current value of the connector
        val = connector['val']
        if val is None: # the case when the connector has not been initialized
            informant, connector['val'] = source, value
            if name is not None: # some key connectors have their names, and whenever their internal states change, we let them print them out
                print(name, '=', value)
            # once the connector gets a new value, it should inform all of the constraints where it involves in
            inform_all_except(source, 'new_val', constraints)
        else:
            """ protection mechanism: before we want to introduce new values from another sources, we have to explicitly inform the connector to forget its internal state(what it already has). Otherwise, the conflict triggers an alarm.
            """
            if val != value:
                print('Contradiction detected:', val, 'vs', value)

    def forget_value(source):
        nonlocal informant
        """ If the connector has the value from userA, but now userB asks the connector to forget its value, the request will be ignored. Because the connector has userA recorded as the informant, userB as the source, and they don't match.
        Further thought, if userB wants to update this connector, he/she has to request userA to inform the connector to forget userA's input first.
        The forget_value function only works when the one requesting for internal state initialization is the one who set the connector's value before.
        """
        if informant == source:
            informant, connector['val'] = None, None
            if name is not None:
                print(name, 'is forgotton')
            inform_all_except(source, 'forget', constraints)
    
    connector = {'val': None,
                 'set_val': set_value,
                 'forget': forget_value,
                 'has_val': lambda: connector['val'] is not None,
                 'connect': lambda source: constraints.append(source)}

    return connector


def make_ternary_constraint(a, b, c, ab, ca, cb):
    """The constraint that ab(a, b) = c and ca(c, a) = b and cb(c, b) = a."""
    
    def new_value():
        """check connectors a, b, c's status, there should exist one who doesn't have a value right now and that's when the new value message coming in
        """
        av, bv, cv = [connector['has_value']() for connector in (a, b, c)]
        if av and bv: # connectors a and b have values but c doesn't
            c['set_val'](constraint, ab(a['val'], b['val']))
        elif av and cv:
            b['set_val'](constraint, ca(c['val'], a['val']))
        elif bv and cv:
            a['set_val'](constraint, cb(c['val'], b['val']))

    def forget_value():
        for connector in (a, b, c):
            connector['forget'](constraint)

    # messages the constraint accepts and corresponding actions it takes
    constraint = {'new_val': new_value, 'forget': forget_value}
    # let connectors a, b, and c engage in this constraint
    for connector in (a, b, c):
        connector['connect'](constraint)

    return constraint


