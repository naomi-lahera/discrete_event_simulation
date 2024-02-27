from sim import Series_Server
import numpy as np
import random
from statistics import mean
total_Na = 0
total_t = 0
total_tiempo_faltante = 0
total_promedio_tiempo_sistema = 0

n = 500
for _ in range(0, n):
    # Cuando el parametro scale de la distribucion exponencial es 1 se antienden un promedio de 5 clientes
    params = [np.random.randint(5, 10) for _ in range(100)]
    poisson_param = 5
    total_time = 480 # 8 horas
    NA, t, A, D = Series_Server(total_time, poisson_param , params)
    total_Na += NA
    total_t += t
    total_tiempo_faltante += t - total_time
    total_promedio_tiempo_sistema += mean([D[i] - A[0][i] for i in range(NA)])
    
print(f"Promedio de clientes atendidos: {total_Na / n}")
print(f"Promedio de tiempo total de simulación: {total_t / n}")
print(f"Promedio de tiempo faltante: {total_tiempo_faltante / n}")
print(f"Promedio de tiempo de un cliente en el sistema: {total_promedio_tiempo_sistema / n}")
    
# Para calcular promedios, puedes usar el código proporcionado anteriormente
print('varianza: ', np.var([D[i] - A[0][i] for i in range(NA)]))