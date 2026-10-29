---
title: Funciones de agregado (Lakehouse v1)
description: "Funciones de agregado de SQL de Lakehouse v1: resumen de filas con SUM, AVG, MIN, MAX, COUNT y agregados estadísticos."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/index.md
---

Las funciones de agregado son herramientas esenciales de SQL que permiten realizar cálculos sobre un conjunto de valores y devolver un único resultado.

Estas funciones le ayudan a extraer y resumir datos de las bases de datos para obtener información valiosa. 

| Nombre de la función                                             | Qué hace                                                                     | 
|------------------------------------------------------------------|------------------------------------------------------------------------------|
| [ANY](aggregate-any)                                             | Comprueba si alguna fila cumple la condición especificada                    | 
| [APPROX_COUNT_DISTINCT](aggregate-approx-count-distinct)         | Estima el número de valores distintos con HyperLogLog                        | 
| [ARG_MAX](aggregate-arg-max)                                     | Encuentra el valor de arg correspondiente al valor máximo de val             | 
| [ARG_MIN](aggregate-arg-min)                                     | Encuentra el valor de arg correspondiente al valor mínimo de val             | 
| [AVG_IF](aggregate-avg-if)                                       | Calcula el promedio de las filas que cumplen una condición                   | 
| [ARRAY_AGG](aggregate-array-agg)                                 | Convierte todos los valores de una columna en una matriz                     |
| [AVG](aggregate-avg)                                             | Calcula el valor promedio de una columna específica                          | 
| [COUNT_DISTINCT](aggregate-count-distinct)                       | Cuenta el número de valores distintos de una columna                         | 
| [COUNT_IF](aggregate-count-if)                                   | Cuenta las filas que cumplen una condición especificada                      | 
| [COUNT](aggregate-count)                                         | Cuenta el número de filas que cumplen ciertos criterios                      | 
| [COVAR_POP](aggregate-covar-pop)                                 | Devuelve la covarianza poblacional de un conjunto de pares de números        | 
| [COVAR_SAMP](aggregate-covar-samp)                               | Devuelve la covarianza muestral de un conjunto de pares de números           | 
| [GROUP_ARRAY_MOVING_AVG](aggregate-group-array-moving-avg)       | Devuelve una matriz con elementos que calculan el promedio móvil de los valores de entrada |
| [GROUP_ARRAY_MOVING_SUM](aggregate-group-array-moving-sum)       | Devuelve una matriz con elementos que calculan la suma móvil de los valores de entrada     |
| [HISTOGRAM](aggregate-histogram)                                | Genera un histograma de la distribución de los datos con buckets de igual altura |
| [JSON_ARRAY_AGG](aggregate-json-array-agg)                      | Convierte valores en una matriz JSON, omitiendo los NULL                    | 
| [JSON_OBJECT_AGG](aggregate-json-object-agg)                    | Convierte pares clave-valor en un objeto JSON                               | 
| [KURTOSIS](aggregate-kurtosis)                                   | Calcula la curtosis en exceso de un conjunto de valores                      | 
| [MAX_IF](aggregate-max-if)                                       | Encuentra el valor máximo de las filas que cumplen una condición            | 
| [MAX](aggregate-max)                                             | Encuentra el valor más grande de una columna específica                      | 
| [MEDIAN](aggregate-median)                                       | Calcula la mediana de una columna específica                                 | 
| [MEDIAN_TDIGEST](aggregate-median-tdigest)                       | Calcula la mediana de una columna específica con el algoritmo t-digest       | 
| [MIN_IF](aggregate-min-if)                                       | Encuentra el valor mínimo de las filas que cumplen una condición            | 
| [MIN](aggregate-min)                                             | Encuentra el valor más pequeño de una columna específica                     | 
| [QUANTILE_CONT](aggregate-quantile-cont)                         | Calcula el cuantil interpolado de una columna específica                     |
| [QUANTILE_DISC](aggregate-quantile-disc)                         | Calcula el cuantil de una columna específica                                 | 
| [QUANTILE_TDIGEST](aggregate-quantile-tdigest)                   | Calcula el cuantil con el algoritmo t-digest                                 |
| [QUANTILE_TDIGEST_WEIGHTED](aggregate-quantile-tdigest-weighted) | Calcula el cuantil ponderado con el algoritmo t-digest                       |
| [RETENTION](aggregate-retention)                                 | Calcula la retención de un conjunto de eventos                               | 
| [SKEWNESS](aggregate-skewness)                                   | Calcula la asimetría de un conjunto de valores                               | 
| [STDDEV_POP](aggregate-stddev-pop)                               | Calcula la desviación estándar poblacional de una columna                    | 
| [STDDEV_SAMP](aggregate-stddev-samp)                             | Calcula la desviación estándar muestral de una columna                       | 
| [STRING_AGG](aggregate-string-agg)                               | Convierte a String todos los valores no NULL, separados por el delimitador   |
| [SUM_IF](aggregate-sum-if)                                       | Suma los valores de una columna específica que cumplen una condición         | 
| [SUM](aggregate-sum)                                             | Suma los valores de una columna específica                                   | 
| [WINDOW_FUNNEL](aggregate-windowfunnel)                          | Analiza el comportamiento de los usuarios en una secuencia de eventos ordenada en el tiempo |
