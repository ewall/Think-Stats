# Example 3-11

import Cdf
from ex3_9 import weights_cdf

def Median(cdf):
    return cdf.Percentile(50)

def Interquartile(cdf):
    return cdf.Percentile(75) - cdf.Percentile(25)
    
print "25th:", weights_cdf.Percentile(25)
print "50th:", Median(weights_cdf)
print "75th:", weights_cdf.Percentile(75)
print "IQR: ",Interquartile(weights_cdf)
#print "Mean:",int(round(weights_cdf.Mean()))

# yes, the distribution looks symmetric, since the median is halfway between Ql & Qu