---
title: JARO_WINKLER (Lakehouse v1)
description: JARO_WINKLER — calcula la distancia de Jaro-Winkler entre dos cadenas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/jaro-winkler.md
---

Calcula la [Distancia de Jaro-Winkler](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance) entre dos cadenas. Se usa comúnmente para medir la similitud entre cadenas, con valores que van de 0.0 (completamente distintas) a 1.0 (cadenas idénticas). 

## Sintaxis de Analyze

```python
func.jaro_winkler(<string1>, <string2>)
```

## Ejemplos de Analyze

```python
func.jaro_winkler('databend', 'Databend')
┌───────────────────────────────────────────┐
│ func.jaro_winkler('databend', 'Databend') │
├───────────────────────────────────────────┤
│                        0.9166666666666666 │
└───────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
JARO_WINKLER(<string1>, <string2>)
```

## Ejemplos de SQL

La función JARO_WINKLER devuelve un valor FLOAT64 que representa la similitud entre las dos cadenas de entrada. El valor devuelto sigue estas reglas:

- Rango de similitud: el resultado va de 0.0 (completamente distintas) a 1.0 (idénticas).

    ```sql
    SELECT JARO_WINKLER('databend', 'Databend') AS similarity;

    ┌────────────────────┐
    │     similarity     │
    ├────────────────────┤
    │ 0.9166666666666666 │
    └────────────────────┘

    SELECT JARO_WINKLER('databend', 'database') AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │        0.9 │
    └────────────┘
    ```
- Tratamiento de NULL: si string1 o string2 es NULL, el resultado es NULL.

    ```sql
    SELECT JARO_WINKLER('databend', NULL) AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │ NULL       │
    └────────────┘
    ```
- Cadenas vacías:
    - Al comparar dos cadenas vacías se devuelve 1.0.

    ```sql
    SELECT JARO_WINKLER('', '') AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │          1 │
    └────────────┘
    ```
    - Al comparar una cadena vacía con una cadena no vacía se devuelve 0.0.

    ```sql
    SELECT JARO_WINKLER('databend', '') AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │          0 │
    └────────────┘
    ```
