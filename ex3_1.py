# Example 3-1

import Pmf, myplot

def BiasPmf(pmf, name, invert=False):
    biased = pmf.Copy()
    biased.name = name
    
    for x,p in pmf.Items():
        if invert:
            biased.Mult(x, 1.0/x)
        else:
            biased.Mult(x, x)

    biased.Normalize()
    return biased    

def UnbiasPmf(pmf, name):
    return BiasPmf(pmf, name, True)

def main():
    distro = { 7:8, 12:8, 17:14, 22:4, 27:6, 32:12, 37:8, 42:3, 47:2 }
    
    pmf = Pmf.MakePmfFromDict(distro, 'actual')
    biased_pmf = BiasPmf(pmf, 'observed')
    unbiased_pmf = UnbiasPmf(pmf, 'unbiased')
    
    for p in [pmf, biased_pmf, unbiased_pmf]:
        print p.name, "mean = {:.3f}".format(p.Mean())
        print p.name, "var = {:.3f}".format(p.Var())

    myplot.Pmfs([pmf, biased_pmf])
    myplot.Show(xlabel='Class Size', ylabel='PMF')

if __name__ == '__main__':
    main()