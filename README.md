# Proyecto: Simulación de Eventos Discretos

Este proyecto tiene como objetivo desarrollar una simulación de eventos discretos para analizar y entender mejor ciertos fenómenos. A través de este trabajo, buscamos aplicar los principios de la simulación de eventos discretos para modelar y experimentar con estos fenómenos, y obtener resultados que nos ayuden a tomar decisiones informadas.

El proyecto debe ser entregado en un repositorio público de GitHub. Este repositorio debe contener tanto el código fuente de tu simulación como el informe del proyecto en LaTeX. Asegúrese de que el repositorio esté bien organizado y que tanto el código como el informe sean fácilmente accesibles.

# Estructura del informe

## S1 Introducción

- Breve descripción del proyecto
    En el presente proyecto simularemos n servidores conectados en serie, con el siguiente funcionamiento:
    Cuando un cliente llega, entra en servicio con el servidor i si ese servidor está libre, o se une a la cola del servidor i en caso contrario. Luego al terminar el servicio en el servidor i pasa al servidor i + 1. Luego de consumir el servicio de los n servidores el cliente abandona el sisitema.

- Objetivos y metas
    Nuestro objetivo al simular esta sistema es saber la media del tiempo que le toma a un cliente entrar y salir del sistema, así como la noción del rango de timepo que excede la salida del último cliente.

- El sistema específico a simular y las variables de interés que cada equipo debe analizar se les hará saber por esta misma vía.
    - sistema: n servidores en serie
    - variables de interes: 
        - NA: Cantidad de clientes que entraron al sistema
        - A: Tiempo en el que los clientes entran a acada servidor
        - D: Tiempo en que los clientes alen del sistema
        - t: Tiempo que toma hacer la simulacion

- Variables que describen el problema
    - n: cantidad de servidores
    - M: Distribucion asociada a la llegada de los clientes
    - Gi: Distribucion asociada al tiempo de que le toma al servidor i atender a un clinete.
    

## S2 Detalles de Implementación

- Pasos seguidos para la implementación
Para modelar el problema e implementar la simulación correspondiente y con ella resolver dicho problema en cuestión debemos definir como sería la misma:

Simulación:
1. Inicialización del sistema: Se establecen variables para los contadores de clientes en cada servidor (n1, n2), tiempos de eventos (tA, t1, t2), contadores de llegadas y salidas (NA, ND), y listas para almacenar tiempos de eventos (A1, A2, D).

2. Generación de tiempos de llegada: Se utiliza np.random.poisson(param_poisson) para generar el tiempo hasta la próxima llegada de un cliente, basado en el parámetro param_poisson que representa la tasa media de llegada de clientes.

3. Bucle principal: El sistema simula el proceso hasta que el tiempo total de simulación (Total_Time) se excede. Dentro de este bucle, se determina el próximo evento basado en los tiempos de llegada y servicio de los clientes en cada servidor.
- Llegada de clientes: Si el tiempo de llegada del próximo cliente es menor que los tiempos de servicio de ambos servidores, se registra un evento de llegada, se incrementa el contador de llegadas (NA), y se actualiza el tiempo de llegada del próximo cliente.

- Finalización de servicio en el servidor 1: Si el tiempo de finalización de servicio en el servidor 1 es menor que el tiempo de finalización de servicio en el servidor 2, se registra un evento de finalización de servicio en el servidor 1, se decrementa el contador de clientes en el servidor 1 y se incrementa el contador de clientes en el servidor 2.

- Finalización de servicio en el servidor 2: Si el tiempo de finalización de servicio en el servidor 2 es menor que el tiempo de finalización de servicio en el servidor 1, se registra un evento de finalización de servicio en el servidor 2, se decrementa el contador de clientes en el servidor 2 y se incrementa el contador de salidas (ND).

4. Procesamiento de clientes restantes: Después de que el tiempo de simulación se excede, el sistema procesa cualquier cliente restante en las colas, siguiendo la misma lógica que en el bucle principal.

5. Resultados: Al final, el sistema retorna el número total de clientes atendidos (NA), el tiempo total de simulación (t), los tiempos de llegada de los clientes en cada servidor (A1, A2) y los tiempos de salida (D).

## S3 Resultados y Experimentos

- Hallazgos de la simulación
- Interpretación de los resultados
- Necesidad de realizar el análisis estadístico de la simulación (Variables de interés)
    - 
- Análisis de parada de la simulación
    - La simulación se detiene cuando el tiempo total de simulación alcanza el límite establecido (Total_Time) o cuando todos los clientes han sido atendidos (NA == ND). Esto permite modelar sistemas que operan durante un período de tiempo fijo o hasta que se satisfaga un número específico de clientes.

    Este modelo es útil para entender cómo se comporta un sistema bajo diferentes condiciones de carga y puede informar decisiones sobre la optimización de la  configuración del sistema, como el número de servidores o la tasa de llegada de clientes.

## S4 Modelo Matemático

- Descripción del modelo de simulación
    El modelo asociado al sistema a simular se asemeja a la estructura de un sistema de colas de servidores en serie con tiempos de servicio variable (Variable Service Time, VST), que es una extensión de los modelos de colas de M/M/c.

    - M/M/c 
        Los modelos M/M/c son una clase de modelos matemáticos que se utilizan para describir sistemas donde los clientes llegan a una cola de servidores, donde    cada servidor puede atender a un solo cliente a la vez.
        - M representa el modelo de interarrival de Markov, que indica que el tiempo entre llegadas de clientes sigue una distribución de Poisson, lo significa que los clientes llegan de manera independiente y a una tasa constante promedio.
        - M (el segundo M) indica que el modelo de servicio es Markov, lo que significa que el tiempo que un servidor tarda en atender a un cliente sigue una distribución exponencial, donde los tiempos de servicio son independientes entre sí y tienen una media constante.
        - c es el número de servidores en el sistema. Este parámetro indica cuántos servidores pueden atender a los clientes simultáneamente.
        Este modelo es particularmente útil para analizar el comportamiento de sistemas con un número fijo de servidores y clientes que llegan a una tasa constante; puede utilizarse para calcular varias métricas importantes del sistema, el tiempo promedio que un cliente pasa en el sistema (W), y la probabilidad de que haya (n) clientes en el sistema (Pn).

- Supuestos y restricciones
    - Supuestos:
        - Tiempos de servicio (Gi): Se asume que los tiempos de servicio en cada uno de los servidores i siguen una distribución específica Gi. Esto significa que    el     tiempo que cada cliente pasa en el servidor i es variable y sigue una distribución estadística determinada.
        - Servidores en serie: Se asume que los servidores están dispuestos en serie, lo que significa que un cliente debe pasar por cada servidor en orden, desde    el     servidor 1 hasta el servidor n, antes de abandonar el sistema.
        Colas: Se asume que cada servidor tiene una cola de clientes. Si un servidor está ocupado cuando un cliente llega, el cliente se une a la cola del  - servidor     correspondiente.
    - Restricciones:
        - Distribución de llegadas (M): Se asume que las llegadas de clientes siguen una distribución específica M. Esto implica que el número de clientes que llegan al  sistema en un intervalo de tiempo específico sigue una distribución determinada, lo que afecta la probabilidad de llegada y la demanda del sistema.
        - Sin Capacidad de Los Servidores: El modelo no implementa una restricción explícita sobre la capacidad de los servidores. Aunque se mantiene un contador de      clientes en servicio para cada servidor, no se aplica una restricción que evite que un servidor atienda a más clientes de lo que podría manejar.
        - Tiempo de Simulación: La simulación continúa hasta que se alcanza el tiempo total especificado (Total_Time) o hasta que todos los clientes han sido atendidos.
    