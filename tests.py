from sim import Series_Server
import random
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

total_Na =   0
total_t =   0
total_tiempo_faltante =   0
total_promedio_tiempo_sistema =   0
tiempos_promedio_clientes = []  # Lista para almacenar el tiempo promedio de cada cliente por simulación
tiempos_finales_simulaciones = []
tiempos_espera = []  # Lista para almacenar los tiempos de espera de los clientes
tiempos_llegada = []
n =   100
total_time =   480 #   8 horas

for _ in range(0, n):
    params = [np.random.randint(5,   10) for _ in range(2)]
    poisson_param =   5
    NA, t, A, D = Series_Server(total_time, poisson_param , params)
    total_Na += NA
    total_t += t
    total_tiempo_faltante += t - total_time
    tiempo_promedio_cliente = mean([D[i] - A[0][i] for i in range(NA)])
    total_promedio_tiempo_sistema += tiempo_promedio_cliente
    tiempos_promedio_clientes.append(tiempo_promedio_cliente)  # Almacenar el tiempo promedio de cada cliente
    tiempos_finales_simulaciones.append(t)  # Almacenar el tiempo final de cada simulación
    # Almacenar los tiempos de espera de los clientes
    for i in range(NA):
        tiempo_espera = D[i] - A[0][i]
        tiempos_espera.append(tiempo_espera)
        tiempos_llegada.append(A[0][i])
    


print(f"Promedio de clientes atendidos: {total_Na / n}")
print(f"Promedio de tiempo total de simulación: {total_t / n}")
print(f"Promedio de tiempo faltante: {total_tiempo_faltante / n}")
print(f"Promedio de tiempo de un cliente en el sistema: {total_promedio_tiempo_sistema / n}")

# Graficar el tiempo promedio de cada cliente en la tienda por simulación
plt.figure(figsize=(10,   6))
plt.plot(tiempos_promedio_clientes, marker='o')
plt.title('Tiempo promedio de cada cliente en la tienda por simulación')
plt.xlabel('Simulación')
plt.ylabel('Tiempo promedio (mins)')
plt.grid(True)
plt.savefig("mi_grafica.png")
plt.show()

# Calcular y mostrar la media de los tiempos finales de las simulaciones
media_tiempos_finales = mean(tiempos_finales_simulaciones)
print(f"Media de los tiempos finales de las simulaciones: {media_tiempos_finales}")

# Graficar los tiempos finales de las simulaciones
plt.figure(figsize=(10,   6))
plt.plot(tiempos_finales_simulaciones, marker='o')
plt.title('Tiempos finales de las simulaciones')
plt.xlabel('Simulación')
plt.ylabel('Tiempo final (horas)')
plt.axhline(y=media_tiempos_finales, color='r', linestyle='-', label=f'Media: {media_tiempos_finales}')
plt.axhline(y=total_time, color='green', linestyle='-', label=f'Tiempo de trabajo: {total_time}')
plt.grid(True)
plt.legend()
plt.savefig("mi_grafica2.png")
plt.show()

# Graficar la relación entre el tiempo de llegada y el tiempo de espera de los clientes
plt.figure(figsize=(10,   6))
plt.scatter(tiempos_llegada, tiempos_espera, alpha=0.5)
plt.title('Relación entre el tiempo de llegada y el tiempo de espera de los clientes')
plt.xlabel('Tiempo de llegada (min)')
plt.ylabel('Tiempo de espera (min)')
plt.grid(True)
plt.savefig("mi_grafica3.png")
plt.show()

# Graficar la distribución de los tiempos de espera de los clientes
plt.figure(figsize=(10,   6))
sns.kdeplot(tiempos_espera, bw_method=0.5, color='g')
plt.title('Distribución de los tiempos de espera de los clientes en la tienda')
plt.xlabel('Tiempo de espera (mins)')
plt.ylabel('Densidad de probabilidad')
plt.grid(True)
plt.savefig("mi_grafica4.png")
plt.show()