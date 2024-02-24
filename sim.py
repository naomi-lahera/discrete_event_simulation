import numpy as np
 
def Series_Server(Total_Time, param_poisson, param_Server1, param_Server2):
    # Parámetros del sistema
    n1, n2 =  0,  0  # Estado inicial del sistema:  0 clientes en cada servidor
    tA, t1, t2 =  0, float('inf'), float('inf')  # Inicializar tiempos de eventos
    NA, ND =  0,  0  # Contadores de llegadas y salidas
    A1, A2, D = [], [], []  # Listas para almacenar tiempos de eventos
    # Bucle principal siempre que puedan llegar cliente
    # Generar el primer tiempo de llegada
    T0 = np.random.poisson(param_poisson)  # Tiempo hasta la próxima llegada
    tA = T0
    t = 0
    while t <= Total_Time:
        # Actualizar el tiempo actual y seleccionar el próximo evento
        if tA < Total_Time and tA <= t1 and tA <= t2:
            # Evento de llegada
            t = tA
            NA +=  1
            n1 +=  1
            A1.append(t)
            # Generar el próximo tiempo de llegada
            T0 = np.random.poisson(param_poisson)  # Tiempo hasta la próxima llegada
            tA = t + T0
            # Si hay espacio en el servidor  1, comienza el servicio
            if n1 ==  1:
                Y1 = np.random.exponential(param_Server1)
                t1 = t + Y1
        elif t1 < tA and t1 <= t2:
            # Evento de finalización de servicio en el servidor  1
            t = t1
            n1 -=  1
            n2 +=  1
            A2.append(t)
            # Si hay espacio en el servidor  2, comienza el servicio
            if n2 ==  1:
                Y2 = np.random.exponential(param_Server2)
                t2 = t + Y2
            # Si hay clientes en el servidor  1, generar el próximo tiempo de servicio
            if n1 >  0:
                Y1 = np.random.exponential(param_Server2)
                t1 = t + Y1
            else:
                t1 = float('inf')
        elif t2 < tA and t2 < t1:
            # Evento de finalización de servicio en el servidor  2
            t = t2
            ND +=  1
            n2 -=  1
            D.append(t)
            # Si hay clientes en el servidor  2, generar el próximo tiempo de servicio
            if n2 >  0:
                Y2 = np.random.exponential(param_Server2)
                t2 = t + Y2
            else:
                t2 = float('inf')
    #Luego de pasado el tiempo de cierre no se reciben más clientes y se terminan de atender los que quedan en las colas       
    while ND < NA:
      
        if t1 <= t2:
            # Evento de finalización de servicio en el servidor  1
            t = t1
            n1 -=  1
            n2 +=  1
            A2.append(t)
            # Si hay espacio en el servidor  2, comienza el servicio
            if n2 ==  1:
                Y2 = np.random.exponential(param_Server2)
                t2 = t + Y2
            # Si hay clientes en el servidor  1, generar el próximo tiempo de servicio
            if n1 >  0:
                Y1 = np.random.exponential(param_Server1)
                t1 = t + Y1
            else:
                t1 = float('inf')
            
        elif t2 < t1:
            # Evento de finalización de servicio en el servidor  2
            t = t2
            ND +=  1
            n2 -=  1
            D.append(t)
            # Si hay clientes en el servidor  2, generar el próximo tiempo de servicio
            if n2 >  0:
                Y2 = np.random.exponential(param_Server2)
                t2 = t + Y2
            else:
                t2 = float('inf')
            
        else:
            break  # No hay más eventos para procesar

    # Imprimir resultados
    print(f"Clientes atendidos: {NA}")
    print(f"Tiempo total de simulación: {t}")
    print(f"Tiempos de llegada en el servidor  1: {len(A1)}")
    print(f"Tiempos de llegada en el servidor  2: {len(A2)}")
    print(f"Tiempos de salida: {len(D)}")

Series_Server(100,5,3,4)