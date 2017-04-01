[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> -0.088672927072602
> This is a greater effect size (about 3x magnitude) than pregnancy length, but still seems rather small.
> ```
    import nsfg
    import math
    def CohensD(group1, group2):
        """
        Returns the Effect size (Cohen's D) between two groups of data.
        :param group1: Pandas series
        :param group2: Pandas series
        :return: float
        """
        diff = group1.mean() - group2.mean()

        n1, n2 = len(group1), len(group2)
        pooled_var = (group1.var() * n1 + group2.var() * n2) / (n1 + n2)
        return diff/math.sqrt(pooled_var)
    preg = nsfg.ReadFemPreg()
    live = preg[preg.outcome == 1]
    firsts = live[live.birthord == 1]
    others = live[live.birthord != 1]
    print(CohensD(firsts.totalwgt_lb, others.totalwgt_lb))
  ```
>