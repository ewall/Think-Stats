# Example 2-5

def PmfMean(pmf):
    mu = 0.0
    for x,p in pmf.Items():
        mu += p * x
    return mu

def PmfVar(pmf,mu=None):
    var = 0.0
    if mu is None:
        mu = PmfMean(pmf)
    for x,p in pmf.Items():
        var += p * (x - mu)**2
    return var
