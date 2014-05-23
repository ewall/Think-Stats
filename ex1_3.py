# Example 1-3

import survey
table = survey.Pregnancies()
table.ReadRecords()
print 'Number of pregnancies', len(table.records)

def Mean(l):
	return float(sum(l)) / len(l)

def Var(l,mu=None):
	if mu is None:
		mu = Mean(l)
	devsqrd = [(x-mu)**2 for x in l]
	return Mean(devsqrd)

births = [rec for rec in table.records if rec.outcome == 1]
print 'Number of live births', len(births)

first_births = [brec for brec in births if brec.birthord == 1]
later_births = [brec for brec in births if brec.birthord > 1]
print 'Number of first births', len(first_births)
print 'Number of later births', len(later_births)

first_birth_gests = [x.prglength for x in first_births]
later_birth_gests = [x.prglength for x in later_births]

mu_firsts = Mean(first_birth_gests)
mu_laters = Mean(later_birth_gests)
print 'Mean gestation of first births', mu_firsts
print 'Mean gestation of later births', mu_laters
print 'Difference in days', (mu_firsts - mu_laters) * 7.0
print 'Difference in hours', (mu_firsts - mu_laters) * 7 * 24.0
