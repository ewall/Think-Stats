# Example 2-7

import descriptive, Pmf, myplot
import matplotlib.pyplot as pyplot

def CondPmf(pmf, wk):
    cond_pmf = pmf.Copy()
    for v in cond_pmf.Values():
        if v < wk:
            cond_pmf.Remove(v)
    cond_pmf.Normalize()
    return cond_pmf

def ShowPlot(firsts, others):
    weeks = range(35, 46)
    probs = {}
    for table in [firsts, others]:
        name = table.pmf.name
        probs[name] = []
        for week in weeks:
            cond = CondPmf(table.pmf, week)
            prob = cond.Prob(week)
            #print week, prob, table.pmf.name
            probs[name].append(prob)
    pyplot.clf()
    for name, ps in probs.iteritems():
        pyplot.plot(weeks, ps, label=name)
        #print name, ps
    myplot.Show(root='conditional',
                xlabel='weeks',
                ylabel='Prob{x $=$ weeks | x $\geq$ weeks}',
                title='Conditional Probability')

def main():
    pool, firsts, others = descriptive.MakeTables()
    firsts.pmf.name = "first"
    print "Probabilty at 39 weeks for first baby: {:.1%}".format(CondPmf(firsts.pmf,39).Prob(39))
    print "Probabilty at 39 weeks for later babies: {:.1%}".format(CondPmf(others.pmf,39).Prob(39))
    ShowPlot(firsts, others)
    
if __name__ == "__main__":
    main()