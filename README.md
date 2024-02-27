# Proyecto: Simulación de Eventos Discretos

Este proyecto tiene como objetivo desarrollar una simulación de eventos discretos para analizar y entender mejor ciertos fenómenos. A través de este trabajo, buscamos aplicar los principios de la simulación de eventos discretos para modelar y experimentar con estos fenómenos, y obtener resultados que nos ayuden a tomar decisiones informadas.

El proyecto debe ser entregado en un repositorio público de GitHub. Este repositorio debe contener tanto el código fuente de tu simulación como el informe del proyecto en LaTeX. Asegúrese de que el repositorio esté bien organizado y que tanto el código como el informe sean fácilmente accesibles.

# Estructura del informe

## S1 Introducción

- Breve descripción del proyecto
- Objetivos y metas
- El sistema específico a simular y las variables de interés que cada equipo debe analizar se les hará saber por esta misma vía.
- Variables que describen el problema

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
- Análisis de parada de la simulación

## S4 Modelo Matemático

- Descripción del modelo de simulación
- Supuestos y restricciones


## Ejercicio a resolver: n servidores en serie

Los clientes llegan a un sistema que tiene n servidores, y las llegadas distribuye M. Cada cliente que llega debe ser atendido primero por el servidor 1 y, al completar el servicio en el servidor 1, el cliente pasa al servidor 2.

Cuando un cliente llega, entra en servicio con el servidor 1 si ese servidor está libre, o se une a la cola del servidor 1 en caso contrario. De manera similar, cuando el cliente completa el servicio en el servidor 1, entra en servicio con el servidor 2 si ese servidor está libre, o se une a su cola y asi sucesivamente. Después de ser atendido en el servidor n, el cliente abandona el sistema.

Los tiempos de servicio en el servidor i ti# discrete_event_simulation

## 2. n servidores en serie

Los clientes llegan a un sistema que tiene n servidores, y las llegadas distribuye M. Cada cliente que llega debe ser atendido primero por el servidor 1 y, al completar el servicio en el servidor 1, el cliente pasa al servidor 2.

Cuando un cliente llega, entra en servicio con el servidor 1 si ese servidor está libre, o se une a la cola del servidor 1 en caso contrario. De manera similar, cuando el cliente completa el servicio en el servidor 1, entra en servicio con el servidor 2 si ese servidor está libre, o se une a su cola y asi sucesivamente. Después de ser atendido en el servidor n, el cliente abandona el sistema.

Los tiempos de servicio en el servidor i tienen la distribución Gi.


## S1 Introducción

- Breve descripción del proyecto
    En el presente proyecto simularemos n servidores conectados en serie, con el siguiente funcionamiento:
    Cuando un cliente llega, entra en servicio con el servidor i si ese servidor está libre, o se une a la cola del servidor i en caso contrario. Luego al terminar el servicio en el servidor i pasa al servidor i + 1. Luego de consumir el servicio de los n servidores el cliente abandona el sisitema.

- Objetivos y metas
    Nuestro objetivo al simular esta sistema es saber la media del tiempo que le toma a un cliente entrar y salir del sistema, así como la noción del rango de timepo que excede la salida del último cliente.
- El sistema específico a simular y las variables de interés que cada equipo debe analizar se les hará saber por esta misma vía.
    - sistema: n servidores en serie
    - variables: 
- Variables que describen el problema
    