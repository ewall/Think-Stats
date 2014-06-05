# Example 3-6

import survey, Cdf
from ex3_3 import PercentileRank
table = survey.Pregnancies()
table.ReadRecords()
births = [rec for rec in table.records if rec.outcome == 1]

first_births = [brec for brec in births if brec.birthord == 1]
later_births = [brec for brec in births if brec.birthord > 1]

first_birth_weights = [x.birthwgt_lb for x in first_births if x.birthwgt_lb < 97]
later_birth_weights = [x.birthwgt_lb for x in later_births if x.birthwgt_lb < 97]

my_weight = 8
my_rank = PercentileRank(first_birth_weights, my_weight)
print "For your birth weight of {0}, you're percentile rank is {1:.2f}%.".format(my_weight, my_rank)

# check percentile with CDF
firsts_cdf = Cdf.MakeCdfFromList(first_birth_weights, 'first birth weights')
if firsts_cdf.Percentile(my_rank) != my_weight:
    print "Are you sure you calculated that right?"

others_rank = PercentileRank(later_birth_weights, my_weight)
diff = abs(my_rank - others_rank)
print "If you were a first baby, you'd rank at {0:.2f}%; a difference of {1:.2f}%.".format(others_rank, diff)

# check again
laters_cdf = Cdf.MakeCdfFromList(later_birth_weights, 'later birth weights')
if laters_cdf.Percentile(others_rank) != my_weight:
    print "You might want to check that again..."