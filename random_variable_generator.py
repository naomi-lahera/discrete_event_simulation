import numpy as np
from enum import Enum

class distribution(Enum):
    poisson = 1,
    binomial = 2

dis = {
    distribution.poisson : lambda : (np.random.geometric(p=0.35, size=10000) ==  1).sum() / 10000,
    distribution.binomial : lambda : np.random.binomial(n=10000, p=0.35, size=1)[0] / 10000
}

# print(distribution.poisson.name, dis[distribution.poisson](0.7))
# print( np.random.binomial(10000, 0.7))
print(distribution.binomial.name, dis[distribution.binomial]())