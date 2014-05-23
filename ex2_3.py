# Example 2-3

from operator import itemgetter

def Mode(h):
	f = 0
	m = None
	for val,freq in h.Items():
		if freq > f:
			f = freq
			m = val
	return m

def AllModes(h):
        return sorted(hist.Items(), key=itemgetter(1), reverse=True)
