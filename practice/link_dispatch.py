


empty = 'empty'

def link(first, rest=empty):
    assert is_link(rest), 'rest must be a list'
    return [first, rest]

def is_link(s):
    return s == empty or (type(s) == list and len(s) == 2 and is_link(s[1]))

def first(s):
    assert is_link(s), 'first only applies to linked list'
    return s[0]

def rest(s):
    assert is_link(s), 'rest only applies to linked list'
    assert len(s) == 2, 'rest only applies to linked list with more than one node'
    return s[1]

def len_link(s):
    if s == empty:
        return 0
    elif rest(s) == empty:
        return 1
    return 1 + len_link(rest(s))

def getitem_link(s, i):
    if i == 0:
        return first(s)
    return getitem_link(rest(s), i - 1)

def join_link(s, separator):
    if s == empty:
        return empty
    elif rest(s) ==  empty:
        return str(first(s))
    return str(first(s)) + separator + join_link(rest(s), separator)

def extend_link(s, t):
    """Return a list with the elements of s followed by those of t"""
    assert is_link(t), 'arguments must be linked lists'
    if s == empty:
        return t
    else:
        return link(first(s), extend(rest(s), t))

def insert_link(s, i, value):
    assert i <= len_link(s) - 1, 'index is out of range'
    if i == 0:
        return link(value, s) 
    else:
        u = s
        for _ in range(i-1):
            u = rest(u) # go i - 1 times
        v = link(value, rest(u))
        u[1] = v
        return s 

def mutable_link():
    def dict_len():
        return len_link(dispatch_dict['contents'])
    def dict_getitem(index):
        return getitem_link(dispatch_dict['contents'], index)
    def dict_push_first(value):
        dispatch_dict['contents'] = link(value, dispatch_dict['contents'])
        return dispatch_dict['contents']
    def dict_pop_first():
        result = first(dispatch_dict['contents'])
        update = rest(dispatch_dict['contents'])
        dispatch_dict['contents'] = update
        return result
    def dict_insert(index, value):
        return insert_link(dispatch_dict['contents'], index, value)
    def dict_display(separator):
        return join_link(dispatch_dict['contents'], separator)
    dispatch_dict = { 'len': dict_len,
                      'getitem': dict_getitem,
                      'push_first': dict_push_first,
                      'pop_first': dict_pop_first,
                      'insert': dict_insert,
                      'str': dict_display, 
                      'contents': empty
                      }
    return dispatch_dict

def api_len(lk):
    return lk['len']()

def api_getitem(lk, index):
    return lk['getitem'](index)

def api_push_first(lk, value):
    return lk['push_first'](value)

def api_pop_first(lk):
    return lk['pop_first']()

def api_insert(lk, index, value):
    return lk['insert'](index, value)

def api_join(lk, separator):
    return lk['str'](separator)

s = mutable_link()
s['len']()





