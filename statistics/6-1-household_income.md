[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

>> Mean: 74278.7075312
> Median: 51226.4544789
> Skewness: 4.94992024443
> Pearson's Skewness: 0.736125801914
> Fraction households below mean: 0.660005879566872
> If the true upper bound is higher, the data will be skewed even more to the right.
> ```
> import thinkstats2, Skewness, PearsonMedianSkewness
> sample_mean = sample.mean()
> sample_median = thinkstats2.Cdf(sample).Value(0.5)
> sample_skewness = Skewness(sample)
> sample_pearson_skewness = PearsonMedianSkewness(sample)
> households_below_mean = len(sample[sample < sample_mean])/len(sample)
> ```
