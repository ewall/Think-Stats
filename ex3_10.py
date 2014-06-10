# Example 3-10

import random, Pmf, Cdf, myplot

size = 10000
lst = [random.random() for i in range(size)]
lst_pmf = Pmf.MakePmfFromList(lst)
lst_cdf = Cdf.MakeCdfFromList(lst)

myplot.Clf()
myplot.Pmf(lst_pmf)
myplot.Show(title='PMF of {0} randoms'.format(size))

myplot.Clf()
myplot.Cdf(lst_cdf)
myplot.Show(title='CDF of {0} randoms'.format(size))

# yes, the distribution is uniform