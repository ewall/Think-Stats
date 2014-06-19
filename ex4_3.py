# Example 4-3

import random, Cdf, myplot

def paretovariate(size, alpha, xmin):
    return [(random.paretovariate(alpha)*xmin) for i in range(size)]

def main():
    sz, alph, exem = 1000, 1.7, 100   
    lst = paretovariate(sz, alph, exem)
    lst_cdf = Cdf.MakeCdfFromList(lst)
    
    myplot.Clf()
    myplot.Cdf(lst_cdf, complement=True, xscale='log', yscale='log')
    myplot.Show(title='CCDF of {0} random paretovariates'.format(sz))

if __name__=='__main__':
    main()
    
# the CDF looks okay, but plotting on log-log scale doesn't make a strait line :(