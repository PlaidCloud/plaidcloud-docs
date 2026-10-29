---
title: JARO_WINKLER (Lakehouse v1)
description: JARO_WINKLER — calcula a distância de Jaro-Winkler entre duas cadeias de caracteres.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/jaro-winkler.md
---

Calcula a [Distância de Jaro-Winkler](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance) entre duas cadeias de caracteres. É normalmente utilizada para medir a semelhança entre cadeias de caracteres, com valores que variam entre 0.0 (completamente diferentes) e 1.0 (cadeias idênticas). 

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

## Exemplos SQL

A função JARO_WINKLER devolve um valor FLOAT64 que representa a semelhança entre as duas cadeias de caracteres de entrada. O valor devolvido segue estas regras:

- Intervalo de semelhança: o resultado varia entre 0.0 (completamente diferentes) e 1.0 (idênticas).

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
- Cadeias de caracteres vazias:
    - Comparar duas cadeias de caracteres vazias devolve 1.0.

    ```sql
    SELECT JARO_WINKLER('', '') AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │          1 │
    └────────────┘
    ```
    - Comparar uma cadeia de caracteres vazia com uma não vazia devolve 0.0.

    ```sql
    SELECT JARO_WINKLER('databend', '') AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │          0 │
    └────────────┘
    ```
