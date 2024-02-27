import numpy as np
from enum import Enum

class distribution(Enum):
<<<<<<< HEAD
    poisson = 1,
    binomial = 2

dis = {
    distribution.poisson : lambda : (np.random.geometric(p=0.35, size=10000) ==  1).sum() / 10000,
    distribution.binomial : lambda : np.random.binomial(n=10000, p=0.35, size=1)[0] / 10000
}

# print(distribution.poisson.name, dis[distribution.poisson](0.7))
# print( np.random.binomial(10000, 0.7))
print(distribution.binomial.name, dis[distribution.binomial]())
=======
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

>>>>>>> 65df55b13a5e76e067fede92c754b923965ab6da
