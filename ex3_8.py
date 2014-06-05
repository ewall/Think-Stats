# Example 3-8

from relay import ConvertPaceToSpeed

print "Percentile rank among all runners, 97 out of 1633: {:.2%}.".format(97/1633.0)
print "Percentile rank among M4049 runners, 26, out of 256: {:.2%}.".format(26/256.0)
print "His speed was {:.2f}mph.".format(ConvertPaceToSpeed("6:53"))

print "To rank 26th in her division, his rival will need to run at {:.2f}mph.".format(ConvertPaceToSpeed("6:28"))