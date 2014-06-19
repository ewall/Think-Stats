# Example 4-1

import random, Cdf, myplot

size = 44
lst = [random.expovariate(32.6) for i in range(size)]
lst_cdf = Cdf.MakeCdfFromList(lst)

myplot.Clf()
myplot.Cdf(lst_cdf, complement=True, xscale='linear', yscale='log')
myplot.Show(title='CCDF of {0} random expovariates'.format(size))