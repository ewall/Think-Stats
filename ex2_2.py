# Example 2-2

from ex1_3 import *

def Dev(l,mu=None,var=None):
	if mu is None:
		mu = Mean(l)
	if var is None:
		var = Var(l,mu)
	return var**(0.5)

print
print 'StdDev/weeks of first baby gestation', Dev(first_birth_gests,mu_firsts)
print 'StdDev/weeks of later baby gestation', Dev(later_birth_gests,mu_laters)
