[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

>> Pearson: 0.0688263542919, Spearman: 0.0945995730681
> ```
> def pearson(a, b):
>     p = ((a - a.mean()) * (b - b.mean())) / (a.std() * b.std())
>     return sum(p)/len(p)
>
> pearsons_corr = pearson(ages, birthweights)
> spearmans_corr = pearson(ages.rank(), birthweights.rank())
>
> bins = np.arange(5, 50, 5)
> indices = np.digitize(ages, bins)
> groups = live.groupby(indices)
>
> age_groups = [group.agepreg.mean() for i, group in groups]
> cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups]
>
> for percent in [75, 50, 25]:
>     birthweight_percentiles = [cdf.Percentile(percent) for cdf in cdfs]
>     label = '%dth' % percent
>     thinkplot.Plot(age_groups, birthweight_percentiles, label=label)
>
> thinkplot.Config(xlabel='Age)',ylabel='Birthweight',axis=[5, 50, 5, 10],legend=False)
> ```

