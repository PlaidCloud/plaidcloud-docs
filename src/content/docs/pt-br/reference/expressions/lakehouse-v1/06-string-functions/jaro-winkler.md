---
title: JARO_WINKLER (Lakehouse v1)
description: JARO_WINKLER — calcula a distância de Jaro-Winkler entre duas strings.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/jaro-winkler.md
---

Calcula a [Distância de Jaro-Winkler](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance) entre duas strings. É comumente usada para medir a similaridade entre strings, com valores que variam de 0,0 (completamente diferentes) a 1,0 (strings idênticas). 

## Sintaxe do Analyze

```python
func.jaro_winkler(<string1>, <string2>)
```

## Exemplos do Analyze

```python
func.jaro_winkler('databend', 'Databend')
┌───────────────────────────────────────────┐
│ func.jaro_winkler('databend', 'Databend') │
├───────────────────────────────────────────┤
│                        0.9166666666666666 │
└───────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
JARO_WINKLER(<string1>, <string2>)
```

## Exemplos de SQL

A função JARO_WINKLER retorna um valor FLOAT64 que representa a similaridade entre as duas strings de entrada. O valor retornado segue estas regras:

- Intervalo de similaridade: o resultado varia de 0,0 (completamente diferentes) a 1,0 (idênticas).

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
- Tratamento de NULL: se string1 ou string2 for NULL, o resultado é NULL.

    ```sql
    SELECT JARO_WINKLER('databend', NULL) AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │ NULL       │
    └────────────┘
    ```
- Strings vazias:
    - Comparar duas strings vazias retorna 1,0.

    ```sql
    SELECT JARO_WINKLER('', '') AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │          1 │
    └────────────┘
    ```
    - Comparar uma string vazia com uma string não vazia retorna 0,0.

    ```sql
    SELECT JARO_WINKLER('databend', '') AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │          0 │
    └────────────┘
    ```
