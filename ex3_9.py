# Example 3-9

import survey, Cdf, myplot

def Sample(cdf, n):
    #return [cdf.Value(random.random()) for i in range(n)]
    #return random.sample(Cdf.Values(), n)
    return [cdf.Random() for i in range(n)]

table = survey.Pregnancies()
table.ReadRecords()
births = [rec for rec in table.records if rec.outcome == 1]
weights = [x.birthwgt_lb for x in births if x.birthwgt_lb < 97]
weights_cdf = Cdf.MakeCdfFromList(weights, 'birth weights')

sample = Sample(weights_cdf, 10000)
sample_cdf = Cdf.MakeCdfFromList(sample, 'sample weights')

myplot.Clf()
myplot.Cdfs( (weights_cdf, sample_cdf) )
myplot.Show(title='CDF of all birth weights',
            xlabel='weight (lbs)',
            ylabel='cumulative probability')
