# Example 3-2

import relay, Pmf, myplot

def BiasPmf(pmf, v, name=None):
    biased_pmf = pmf.Copy()
    for x, p in biased_pmf.Items():
        biased_pmf.Mult(x, abs(x - v))
    biased_pmf.Normalize()
    return biased_pmf
        
def main():
    results = relay.ReadResults()
    speeds = relay.GetSpeeds(results)
    pmf = Pmf.MakePmfFromList(speeds, 'actual speeds')

    observed = BiasPmf(pmf, 7.5, 'observed speeds')
    myplot.Clf()
    myplot.Hist(observed)
    myplot.Show(title='observed speeds',
                xlabel='speed (mph)',
                ylabel='probability')

if __name__ == '__main__':
    main()
