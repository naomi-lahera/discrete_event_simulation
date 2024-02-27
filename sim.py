import numpy as np
import random
from statistics import mean

def Series_Server(Total_Time, param_poisson, param_Server):    
    # Parámetros del sistema
    n_servidores = len(param_Server)  # Número de servidores
    tA =  0  # Tiempo de llegada
    t_eventos = [float('inf')] * n_servidores  # Inicializar tiempos de eventos para cada servidor
    NA, ND =  0,  0  # Contadores de llegadas y salidas
    A = [[] for _ in range(n_servidores)]  # Listas para almacenar tiempos de llegada en cada servidor
    D = []  # Lista para almacenar tiempos de salida
    clientes_en_servicio = [0] * n_servidores  # Contadores de clientes en servicio para cada servidor

    # Generar el primer tiempo de llegada
    T0 = np.random.poisson(param_poisson)
    tA = T0
    t =  0

    while t + tA <= Total_Time:
        # print('event')
    while t + tA <= Total_Time:
        # Actualizar el tiempo actual y seleccionar el próximo evento
        servidor_actual = np.argmin(t_eventos)  # Encontrar el servidor con el próximo evento
        # t = t_eventos[servidor_actual]

        if tA <= t_eventos[servidor_actual]:
            # Evento de llegada
            print(f'tiempo actual: {t} \n proxima llegada: {tA} \n nuevo tA: {t + tA}')
            t = tA
            print('t: ', t)
            t = tA
            NA +=  1
            clientes_en_servicio[0] +=  1
            A[0].append(t)
            # Generar el próximo tiempo de llegada
            T0 = np.random.poisson(param_poisson)
            # print(f'tiempo actual: {t} \\n proxima llegada: {T0} \\n nuevo tA: {t + T0}')
            tA = T0
            tA = t + T0
            # Si hay espacio en el servidor, comienza el servicio
            if clientes_en_servicio[0] ==  1:
                Y = np.random.exponential(param_Server[0])
                t_eventos[0] = Y
                
        else:
            print(f'tiempo actual: {t} \n proxima llegada: {t_eventos[servidor_actual]} \n nuevo t: {t + t_eventos[servidor_actual]}')
            t += t_eventos[servidor_actual]
            # print('t: ', t)
            clientes_en_servicio[servidor_actual] -=  1
            # Si hay clientes en el servidor, generar el próximo tiempo de servicio
            if clientes_en_servicio[servidor_actual] >  0:
                Y = np.random.exponential(param_Server[servidor_actual])
                t_eventos[servidor_actual] = Y
            else:
                t_eventos[servidor_actual] = float('inf')
                
            if servidor_actual >= n_servidores - 1:
                # Evento de finalización de servicio
                ND +=  1
                D.append(t)
                # print('tiempo en el sistema: ', t - A[0][len(D) - 1])
            else:
                clientes_en_servicio[servidor_actual + 1] +=  1
                A[servidor_actual + 1].append(t)
                # Si hay espacio en el servidor, comienza el servicio
                if clientes_en_servicio[servidor_actual + 1] ==  1:
                    Y = np.random.exponential(param_Server[servidor_actual + 1])
                    t_eventos[servidor_actual + 1] = Y

    # Procesar clientes restantes
    while ND < NA:
        # print('event without time')
        servidor_actual = np.argmin(t_eventos)
        print(f'tiempo actual: {t} \n proxima llegada: {t_eventos[servidor_actual]} \n nuevo t: {t + t_eventos[servidor_actual]}')
        t += t_eventos[servidor_actual]
        # print('t: ', t)
        t = t_eventos[servidor_actual]
        clientes_en_servicio[servidor_actual] -=  1
        # Si hay clientes en el servidor, generar el próximo tiempo de servicio
        if clientes_en_servicio[servidor_actual] >  0:
            Y = np.random.exponential(param_Server[servidor_actual])
            t_eventos[servidor_actual] = Y
        else:
            t_eventos[servidor_actual] = float('inf')
            
        if servidor_actual >= n_servidores - 1:
            # Evento de finalización de servicio
            ND +=  1
            D.append(t)
            # print('tiempo en el sistema: ', t - A[0][len(D) - 1])
        else:
            clientes_en_servicio[servidor_actual + 1] +=  1
            A[servidor_actual + 1].append(t)
            # Si hay espacio en el servidor, comienza el servicio
            if clientes_en_servicio[servidor_actual + 1] ==  1:
                Y = np.random.exponential(param_Server[servidor_actual + 1])
                t_eventos[servidor_actual + 1] = Y
                
    return NA, t, A, D

total_Na = 0
total_t = 0
total_tiempo_faltante = 0
total_promedio_tiempo_sistema = 0

n = 1
for _ in range(0, n):
    # Cuando el parametro scale de la distribucion exponencial es 1 se antienden un promedio de 5 clientes
    # Promedio de clientes atendidos: 5.0
    params = [1 for _ in range(1, 50)]
    # atienden de 1 a 20 clientes en 8 horas
    params = [np.random.randint(1, 20) for _ in range(5, 10)]
    print('params: ', params)
    params = [np.random.randint(5, 10) for _ in range(100)]
    poisson_param = 5
    total_time = 480 # 8 horas
    NA, t, A, D = Series_Server(total_time,  np.random.randint(15, 20), params)
    # total_Na += NA
    # total_t += t
    # total_tiempo_faltante += t - 100
    # total_promedio_tiempo_sistema += mean([D[i] - A[0][i] for i in range(NA)])
    NA, t, A, D = Series_Server(total_time, poisson_param , params)
    total_Na += NA
    total_t += t
    total_tiempo_faltante += t - total_time
    total_promedio_tiempo_sistema += mean([D[i] - A[0][i] for i in range(NA)])
    
print(f"Clientes atendidos: {NA}")
print(f"Tiempo total de simulación: {t}")
print(f"Tiempo faltante: {t - 480}")
print(f"Promedio de tiempo de un cliente en el sistema: {sum([D[i] - A[0][i] for i in range(NA)]) / NA}")
    
# print(f"Promedio de clientes atendidos: {total_Na / n}")
# print(f"Promedio de tiempo total de simulación: {total_t / n}")
# print(f"Promedio de tiempo faltante: {total_tiempo_faltante / n}")
# print(f"Promedio de promedio de tiempo de un cliente en el sistema: {total_promedio_tiempo_sistema / n}")
print(f"Promedio de clientes atendidos: {total_Na / n}")
print(f"Promedio de tiempo total de simulación: {total_t / n}")
print(f"Promedio de tiempo faltante: {total_tiempo_faltante / n}")
print(f"Promedio de tiempo de un cliente en el sistema: {total_promedio_tiempo_sistema / n}")
    
# Para calcular promedios, puedes usar el código proporcionado anteriormente
print('varianza: ', np.var([D[i] - A[0][i] for i in range(NA)]))