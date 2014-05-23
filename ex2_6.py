# Example 2-6

import descriptive, Pmf

def ProbBin(pmf,min,max):
    prob = 0.0
    for x,p in pmf.Items():
        if x >= min and x < max:
            prob += p
    return prob

def ProbEarly(pmf):
    """probability of an early birth"""
    # week 37 or earlier
    return ProbBin(pmf, 0, 38)

def ProbOnTime(pmf):
    """probability of an on-time birth"""
    # weeks 38, 39 and 40
    return ProbBin(pmf, 38, 41)

def ProbLate(pmf):
    """probability of a late birth"""
    # week 41 or later
    return ProbBin(pmf, 41, 100)

def PrintRelativeRisks(pmf_firsts, pmf_laters):
    print "Risks:"
    funcs = [ProbEarly, ProbOnTime, ProbLate]
    risks = {}
    for func in funcs:
        for pmf in [pmf_firsts, pmf_laters]:
            prob = func(pmf)
            risks[func.__name__, pmf.name] = prob
            print "  ", func.__name__, "for", pmf.name, " = {:.1%}".format(prob)
        print

    print "Risk ratios (first babies / others):"
    for func in funcs:
        ratio = (risks[func.__name__, 'first babies'] /
                    risks[func.__name__, 'other babies'])
        print "  ",func.__doc__, " = {0:.2f}".format(ratio)

def main():
    
    all_births, first_births, later_births = descriptive.MakeTables()
    later_births.pmf.name = 'other babies'
    
    print " All births:   early   = {:.1%}".format(ProbEarly(all_births.pmf))
    print "               on-time = {:.1%}".format(ProbOnTime(all_births.pmf))
    print "               late    = {:.1%}".format(ProbLate(all_births.pmf))

    PrintRelativeRisks(first_births.pmf, later_births.pmf)

if __name__ == "__main__":
    main()