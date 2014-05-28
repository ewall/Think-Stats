# Example 3-3

def PercentileRank(scores, your_score):
    count = 0
    for score in scores:
        if score <= your_score:
            count += 1
    percentile_rank = 100.0 * count / len(scores)
    return percentile_rank
    
def Percentile(scores, your_rank):
    scores.sort()
    index = your_rank * (len(scores)-1) / 100
    return scores[int(index)]

def main():
    all_scores = [55, 66, 77, 88, 99]
    rank = PercentileRank(all_scores, 88)
    print "If you percentile rank was {0}".format(int(rank))
    print "...your score must have been {0}".format(Percentile(all_scores, rank))

if __name__ == '__main__':
    main()