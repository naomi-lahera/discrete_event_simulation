import numpy as np
from enum import Enum

class distribution(Enum):
    poisson = 1
    binomial = 2
    exponetial = 3
    normal = 4

dis = {
    distribution.poisson : lambda : np.random.poisson(lam=0.76),
    distribution.binomial : lambda : np.random.binomial(n=10000, p=0.3) / 10000,
    distribution.exponetial : lambda : np.random.exponential(scale=0.35),
    distribution.normal: lambda : np.random.normal(loc=0, scale=1)
}

for i in range(1, 5):
    print(dis[distribution(i)]())

