import numpy as np


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
        # Actualizar el tiempo actual y seleccionar el próximo evento
        servidor_actual = np.argmin(t_eventos)  # Encontrar el servidor con el próximo evento
        # t = t_eventos[servidor_actual]

        if tA <= t_eventos[servidor_actual]:
            # Evento de llegada
            t = tA
            NA +=  1
            clientes_en_servicio[0] +=  1
            A[0].append(t)
            # Generar el próximo tiempo de llegada
            T0 = np.random.poisson(param_poisson)
            tA = t + T0
            # Si hay espacio en el servidor, comienza el servicio
            if clientes_en_servicio[0] ==  1:
                Y = np.random.exponential(param_Server[0])
                t_eventos[0] = t + Y
                
        else:
            t = t_eventos[servidor_actual]
            clientes_en_servicio[servidor_actual] -=  1
            # Si hay clientes en el servidor, generar el próximo tiempo de servicio
            if clientes_en_servicio[servidor_actual] >  0:
                Y = np.random.exponential(param_Server[servidor_actual])
                t_eventos[servidor_actual] = t + Y
            else:
                t_eventos[servidor_actual] = float('inf')
                
            if servidor_actual >= n_servidores - 1:
                # Evento de finalización de servicio
                ND += 1
                D.append(t)
            else:
                clientes_en_servicio[servidor_actual + 1] +=  1
                A[servidor_actual + 1].append(t)
                # Si hay espacio en el servidor, comienza el servicio
                if clientes_en_servicio[servidor_actual + 1] ==  1:
                    Y = np.random.exponential(param_Server[servidor_actual + 1])
                    t_eventos[servidor_actual + 1] = t + Y

    # Procesar clientes restantes
    while ND < NA:
        servidor_actual = np.argmin(t_eventos)
        t = t_eventos[servidor_actual]
        clientes_en_servicio[servidor_actual] -=  1
        # Si hay clientes en el servidor, generar el próximo tiempo de servicio
        if clientes_en_servicio[servidor_actual] >  0:
            Y = np.random.exponential(param_Server[servidor_actual])
            t_eventos[servidor_actual] = t + Y
        else:
            t_eventos[servidor_actual] = float('inf')
            
        if servidor_actual >= n_servidores - 1:
            # Evento de finalización de servicio
            ND += 1
            D.append(t)
        else:
            clientes_en_servicio[servidor_actual + 1] +=  1
            A[servidor_actual + 1].append(t)
            # Si hay espacio en el servidor, comienza el servicio
            if clientes_en_servicio[servidor_actual + 1] ==  1:
                Y = np.random.exponential(param_Server[servidor_actual + 1])
                t_eventos[servidor_actual + 1] = t + Y
                
    return NA, t, A, D

