[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> Unbiased Mean: 1.0242051550438309, Biased Mean: 2.4036791006642821
> ```
> import nsfg, thinkstats2, thinkplot, BiasPmf
> resp = nsfg.ReadFemResp()
> num_child_pmf = thinkstats2.Pmf(resp.numkdhh, label='unbiased')
> num_child_bias_pmf = BiasPmf(num_child_pmf, label='biased')
> print(num_child_pmf.Mean(), num_child_bias_pmf.Mean())
> thinkplot.PrePlot(2)
> thinkplot.Pmfs([num_child_pmf, num_child_bias_pmf])
> thinkplot.Config(xlabel='Number Children', ylabel='PMF')
> ```
