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
    