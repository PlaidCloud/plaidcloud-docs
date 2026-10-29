---
title: Optimizador de ubicaciones
description: Elija K sitios de un conjunto de candidatos que minimicen la distancia total o ponderada a un conjunto de puntos de demanda.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/optimization/location-optimizer.md
---

El paso Optimizador de ubicaciones elige **K** sitios de una tabla de ubicaciones candidatas que minimizan la distancia total o ponderada a una tabla de puntos de demanda: un modelo de ubicación de instalaciones de p-mediana resuelto como un programa entero mixto en el solucionador HiGHS de PlaidCloud.

El Optimizador de ubicaciones se ejecuta en un pod de trabajo del flujo de trabajo, con la misma imagen de trabajo que usa [Solucionador](/es/reference/workflow-steps/optimization/solver/), y escribe los resultados en tablas del proyecto.

## Entradas

### Sitios candidatos

La tabla de posibles ubicaciones de sitios, asignada con la misma asignación de columnas de origen/destino, los mismos filtros y la misma agregación que usa toda entrada asignada a una tabla.

### Puntos de demanda

La tabla de puntos cuya distancia al sitio seleccionado más cercano se minimiza, asignada de la misma manera.

### Tabla de distancias (opcional)

Una tabla precalculada de distancias entre candidatos y demanda. Déjela sin definir para que el paso calcule las distancias por sí mismo.

### K

La cantidad de sitios que se seleccionarán de Sitios candidatos.

## Opciones del solucionador

| Opción | Descripción |
| --- | --- |
| Límite de tiempo | Límite opcional del tiempo de ejecución, en segundos. |
| Brecha MIP | Brecha MIP relativa opcional. |
| Habilitar presolve | Permite que el solucionador simplifique el modelo antes de resolverlo. Habilitado de forma predeterminada. |
| Usar recursos personalizados | Define los núcleos de CPU y la memoria del pod de trabajo. |

Una detención por **Límite de tiempo** o por **Brecha MIP** devuelve la mejor solución encontrada dentro de ese límite en lugar del óptimo verdadero: el mismo compromiso que hace [Solucionador](/es/reference/workflow-steps/optimization/solver/#comportamiento-del-estado) con un estado no óptimo. Deje ambos sin definir para resolver hasta la optimalidad completa.

## Salidas

El Optimizador de ubicaciones escribe tres tablas de salida, que deben tener nombres distintos entre sí.

### Tabla de salida de sitios seleccionados

Una fila por cada sitio elegido.

### Tabla de salida de asignaciones

Una fila por cada punto de demanda, con el nombre del sitio seleccionado al que se asignó.

### Tabla de salida de resumen

Una fila con el estado del solucionador, el valor objetivo y los detalles de la ejecución.

## Límites y salvedades

Este paso es un modelo de **p-mediana**: siempre minimiza la distancia total (opcionalmente ponderada) de los puntos de demanda a su sitio seleccionado más cercano. No expresa una puntuación de tipo gravitacional, una fórmula de puntuación personalizada ni ningún objetivo en el que una puntuación más alta sea mejor que una distancia menor. Un problema de selección de sitios que necesite alguna de esas opciones corresponde, en cambio, a un modelo de [Solucionador](/es/reference/workflow-steps/optimization/solver/) creado a mano.

## Relacionado

- [Solucionador](/es/reference/workflow-steps/optimization/solver/): optimización lineal y entera mixta general, para un objetivo de selección de sitios que el modelo de p-mediana fijo de este paso no cubre.
- [Matriz de conversión de Alteryx](/es/reference/alteryx-conversion-matrix/): la herramienta Location Optimizer de Alteryx se convierte a este paso solo en su caso de minimización lineal de la distancia; un núcleo gravitacional o una macro de puntuación personalizada se siguen rechazando.
