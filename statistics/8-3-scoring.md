[Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)

---

>> Used the provided SimulateGame function in the notebook, then created simulate games.
> From one simulation with lambda = 2, got:
> Mean Error: -0.049000000000000002
> RMSE: 1.466628787389638
> ```
> import numpy as np
> from numpy.random import random
>
> def SimulateGame(lam):
>
>     goals = 0
>     t = 0
>     while True:
>         time_between_goals = random.expovariate(lam)
>         t += time_between_goals
>         if t > 1:
>             break
>         goals += 1
>
>     L = goals
>     return L
>
> def SimulateMultiGames(lam):
>     lams = []
>     for _ in range(1000):
>         lams.append(SimulateGame(lam))
>     mean_error = np.mean([l - lam for l in lams])
>     rmse = RMSE(lams, lam)
>     return mean_error, rmse
>
> print(SimulateMultiGames(2))
> ```
---