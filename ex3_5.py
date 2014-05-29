# Example 3-5

import relay, Cdf, myplot

def main():
    results = relay.ReadResults()
    speeds = relay.GetSpeeds(results)

    # plot the distribution of actual speeds
    cdf = Cdf.MakeCdfFromList(speeds, 'speeds')

    myplot.Cdf(cdf)
    myplot.Show(title='CDF of running speed',
                xlabel='speed (mph)',
                ylabel='cumulative probability')

if __name__ == '__main__':
    main()
