[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> Yes, it is random as the distribution is uniform.
> ```
from numpy.random import random
import thinkstats2, thinkplot
nums = random(1000)
nums_pmf = thinkstats2.Pmf(nums)
nums_cdf = thinkstats2.Cdf(nums)
thinkplot.Pmf(nums_pmf, linewidth=0.05)
thinkplot.Config(xlabel='Random Number (0-1)', ylabel='PMF')
thinkplot.Cdf(nums_cdf)
thinkplot.Config(xlabel='Random Number (0-1)', ylabel='CDF')
```
