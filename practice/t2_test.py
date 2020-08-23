
from math import sqrt
phi = 1/2 + sqrt(5)/2
def improve_test():
    approx_phi = improve(golden_update, square_close_to_successor)
    assert approx_eq(phi, approx_phi), 'phi differs from its approximation'

