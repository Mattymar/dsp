[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

>>
> ```
> import math, thinkstats2
> matplotlib.pyplot as plt
>
> def RMSE(estimates, actual):
>     sq_error = [(estimate-actual)**2 for estimate in estimates]
>     mean_sq_error = np.mean(sq_error)
>     return math.sqrt(mean_sq_error)
>
> def estimate_ex(n, m):
>     lam = 2
>     means = []
>     for _ in range(m):
>         xs = np.random.exponential(1.0/lam, n)
>         L = 1 / np.mean(xs)
>         means.append(L)
>     cdf = thinkstats2.Cdf(means)
>     ci = cdf.Percentile(5), cdf.Percentile(95)
>     SE = RMSE(means, lam)
>     return ci, SE
>
> ci, SE = estimate_ex(10, 1000)
> # ci: (1.2661202547644992, 3.6579749328596063)
> # SE: 0.743722445927758
>
> n = list(range(5, 200))
> SE = []
> for i in n:
>     SE.append(estimate_ex(i, 1000)[1])
>
> plt.plot(n, SE)
> ```
