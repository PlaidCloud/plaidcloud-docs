---
title: Solucionador
description: Resuelva problemas de optimización LP y MIP a partir de los datos de tablas del flujo de trabajo.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/optimization/solver.md
---

El paso Solucionador resuelve problemas de programación lineal y de programación entera mixta a partir de tablas de PlaidCloud. Úselo cuando un flujo de trabajo deba elegir valores que minimicen o maximicen un objetivo y cumplan restricciones lineales.

El Solucionador se ejecuta en un pod de trabajo del flujo de trabajo y escribe los resultados en tablas del proyecto.

## Entradas

Configure cuatro tablas de entrada. Cada entrada tiene una tabla de origen, una asignación de datos y filtros. PlaidCloud traduce esa configuración a la consulta de base de datos que se usa para leer cada entrada, de modo que la selección ocurre antes de que el Solucionador reciba las filas.

### Variables

Una fila por cada variable de decisión.

| Columna | Descripción |
| --- | --- |
| `variable_id` | Nombre único de la variable que usan las demás tablas de entrada. |
| `lower_bound` | Valor mínimo. Déjelo en blanco para no tener límite inferior. |
| `upper_bound` | Valor máximo. Déjelo en blanco para no tener límite superior. |
| `type` | `continuous`, `integer` o `binary`. Las variables binarias usan los límites `0` y `1`. |

### Objetivo

Una fila por cada variable con un coeficiente objetivo distinto de cero.

| Columna | Descripción |
| --- | --- |
| `variable_id` | Variable de la entrada Variables. |
| `coefficient` | Coeficiente objetivo de esa variable. |

Las variables que faltan en esta tabla usan el coeficiente `0`.

### Restricciones

Una fila por cada restricción lineal.

| Columna | Descripción |
| --- | --- |
| `constraint_id` | Nombre único de la restricción que usa la entrada Coeficientes. |
| `lower_bound` | Actividad mínima permitida. Déjelo en blanco para no tener límite inferior. |
| `upper_bound` | Actividad máxima permitida. Déjelo en blanco para no tener límite superior. |

Defina el mismo límite inferior y superior para una restricción de igualdad.

### Coeficientes

Matriz dispersa de coeficientes de restricciones.

| Columna | Descripción |
| --- | --- |
| `constraint_id` | Restricción de la entrada Restricciones. |
| `variable_id` | Variable de la entrada Variables. |
| `coefficient` | Coeficiente de esa variable en esa restricción. |

## Opciones del solucionador

| Opción | Descripción |
| --- | --- |
| Dirección del objetivo | Elija Minimizar o Maximizar. |
| Límite de tiempo | Límite opcional del tiempo de ejecución, en segundos. |
| Brecha MIP | Brecha MIP relativa opcional para problemas enteros mixtos. |
| Habilitar presolve | Permite que el solucionador simplifique el modelo antes de resolverlo. |
| Usar recursos personalizados | Define los núcleos de CPU y la memoria del pod de trabajo. |

## Salidas

El Solucionador escribe tres tablas de salida.

### Tabla de solución

Contiene una fila por variable con el valor resuelto, los límites, el tipo de variable, el coeficiente objetivo y el costo reducido cuando está disponible.

### Tabla de resultados de restricciones

Contiene una fila por restricción con la actividad, los límites, la holgura y el valor dual cuando está disponible.

### Tabla de resumen

Contiene una fila con el estado del solucionador, el valor objetivo, el tiempo de ejecución, la brecha MIP, la cota dual MIP, el número de nodos, el número de iteraciones, el número de variables y el número de restricciones.

## Comportamiento del estado

Una resolución óptima completa el paso correctamente. Si el solucionador devuelve una solución utilizable con un estado no óptimo, el paso termina con una advertencia y aun así escribe las tablas de salida. Si no hay ninguna solución utilizable, el paso falla con el mensaje de estado del solucionador.
