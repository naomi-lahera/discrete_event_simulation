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

### La Simulación:
El programa proporcionado simula un sistema de servidores en serie con el objetivo de analizar el comportamiento de los clientes a través de este sistema durante un tiempo total especificado (Total_Time). A continuación se mostrará la descripción paso a paso de lo que hace el programa:

1. Inicialización: Al inicio, el programa establece varios parámetros y estructuras de datos necesarias para el funcionamiento del sistema de servidores. Esto incluye el número de servidores (n_servidores), tiempos de llegada de los clientes (tA), tiempos de eventos para cada servidor (t_eventos), contadores de llegadas (NA) y salidas (ND), y listas para almacenar tiempos de llegada y salida de los clientes (A y D). También se inicializan contadores para los clientes en servicio en cada servidor (clientes_en_servicio).
2. Generación del primer tiempo de llegada: Se genera el primer tiempo de llegada (T0) utilizando la distribución de Poisson (param_poisson), que modela el tiempo entre llegadas de clientes.
3. Bucle principal del programa: El programa entra en un bucle que se ejecuta hasta que el tiempo total simulado (Total_Time) se haya alcanzado. Dentro de este bucle, se realizan las siguientes operaciones:
- Selección del próximo evento: Se determina el servidor con el próximo evento (ya sea una llegada o una salida) basado en el tiempo de eventos mínimo.
- Evento de llegada: Si el tiempo de llegada (tA) es menor o igual al tiempo del próximo evento, se procesa un evento de llegada. Esto implica actualizar el tiempo actual (t), incrementar el contador de llegadas (NA), y registrar el tiempo de llegada en el servidor correspondiente. Además, se genera el próximo tiempo de llegada (T0) y se actualiza el tiempo de llegada (tA).
- Evento de salida: Si no es un evento de llegada, se procesa un evento de salida. Esto implica actualizar el tiempo actual (t), disminuir el contador de clientes en servicio para el servidor seleccionado, y actualizar el tiempo del próximo evento para ese servidor. Si el servidor tiene clientes en servicio, se genera un nuevo tiempo de servicio utilizando una distribución exponencial (param_Server).
4. Manejo de clientes restantes: Después de que el bucle principal se completa, se procesan cualquier cliente restante que aún no haya salido del sistema. Esto se hace de manera similar al procesamiento de eventos de salida dentro del bucle principal.
5. Retorno de resultados: Finalmente, el programa retorna el número total de llegadas (NA), el tiempo total simulado (t), y las listas de tiempos de llegada y salida de los clientes (A y D).

## S3 Resultados y Experimentos

### Hallazgos de la simulación:

- Total de Llegadas (NA): El número total de clientes que llegaron durante la simulación. Este valor es una medida de la carga en el sistema.

- Tiempo Actual (t): El último tiempo en el que se generó un evento. Este valor indica cuánto tiempo se simuló el sistema.

- Tiempos de Llegada (A): Una lista de listas donde cada sublista contiene los tiempos de llegada de los clientes a cada servidor. Esto ayuda a entender cómo se distribuyen los clientes entre los servidores.

- Tiempos de Salida (D): Una lista de los tiempos en los que los clientes fueron atendidos y salieron del sistema. Esto ayuda a entender la eficiencia del sistema en términos de tiempo de espera y tiempo de servicio.

### Interpretación de los resultados
- En este caso mostramos, por cada simulacion, el tiempo de espera promedio de los clientes en la tienda.
![](.\informe\mi_grafica.png)
- En este caso observamos una comparación entre la media del tiempo en que las simulaciones acabaron, el tiempo que se tenia para mantener el sistema funcionando y los valores reales obtenidos por las simulaciones. Como se puede pareciar, la media se queda por debajo de la hora de cierre.
![](.\informe\mi_grafica2.png)
- En el gráfico que se muestra a continuación es posible apreciar la relación que existe entre la hora de llegada y el tiempo de espera de los clientes en el sistema
![](.\informe\mi_grafica3.png)
- Aqui podemos ver una posible distribución que pueden seguir los tiempos de espera de los clientes en la tienda.
![](.\informe\mi_grafica4.png)

- Necesidad de realizar el análisis estadístico de la simulación (Variables de interés)
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
        - Distribución de llegadas (M): Se asume que las llegadas de clientes siguen una distribución específica M. Esto implica que el número de clientes que llegan al  sistema en un intervalo de tiempo específico sigue una distribución determinada.
        - Tiempos de servicio (Gi): Se asume que los tiempos de servicio en cada uno de los servidores i siguen una distribución específica Gi. Esto significa que    el     tiempo que cada cliente pasa en el servidor i es variable y sigue una distribución estadística determinada.
        - Servidores en serie: Se asume que los servidores están dispuestos en serie, lo que significa que un cliente debe pasar por cada servidor en orden, desde    el     servidor 1 hasta el servidor n, antes de abandonar el sistema.
        Colas: Se asume que cada servidor tiene una cola de clientes. Si un servidor está ocupado cuando un cliente llega, el cliente se une a la cola del  - servidor     correspondiente.
    - Restricciones:
        - Sin Capacidad de Los Servidores: El modelo no implementa una restricción explícita sobre la capacidad de los servidores. Aunque se mantiene un contador de      clientes en servicio para cada servidor, no se aplica una restricción que evite que un servidor atienda a más clientes de lo que podría manejar.
        - Tiempo de Simulación: La simulación continúa hasta que se alcanza el tiempo total especificado (Total_Time) o hasta que todos los clientes han sido atendidos.
    