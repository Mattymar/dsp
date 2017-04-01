[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> 0.342746837631
> ```
import scipy.stats
>>
mu = 178
sigma = 7.7
inch_to_cm = 2.54
>>
heights_dist = scipy.stats.norm(loc=mu, scale=sigma)
>>
low_height = 70 * inch_to_cm
high_height = 73 * inch_to_cm
>>
print(heights_dist.cdf(high_height) - heights_dist.cdf(low_height))
```
