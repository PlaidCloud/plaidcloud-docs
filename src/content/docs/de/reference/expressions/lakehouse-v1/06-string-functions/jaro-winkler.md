---
title: JARO_WINKLER (Lakehouse v1)
description: JARO_WINKLER – berechnet die Jaro-Winkler-Distanz zwischen zwei Zeichenfolgen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/jaro-winkler.md
---

Berechnet die [Jaro-Winkler-Distanz](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance) zwischen zwei Zeichenfolgen. Sie wird häufig verwendet, um die Ähnlichkeit zwischen Zeichenfolgen zu messen, mit Werten von 0,0 (völlig unähnlich) bis 1,0 (identische Zeichenfolgen). 

## Analyze-Syntax

```python
func.jaro_winkler(<string1>, <string2>)
```

## Analyze-Beispiele

```python
func.jaro_winkler('databend', 'Databend')
┌───────────────────────────────────────────┐
│ func.jaro_winkler('databend', 'Databend') │
├───────────────────────────────────────────┤
│                        0.9166666666666666 │
└───────────────────────────────────────────┘
```

## SQL-Syntax

```sql
JARO_WINKLER(<string1>, <string2>)
```

## SQL-Beispiele

Die Funktion JARO_WINKLER gibt einen FLOAT64-Wert zurück, der die Ähnlichkeit zwischen den beiden Eingabezeichenfolgen darstellt. Für den Rückgabewert gelten folgende Regeln:

- Ähnlichkeitsbereich: Das Ergebnis reicht von 0,0 (völlig unähnlich) bis 1,0 (identisch).

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
- Behandlung von NULL: Ist string1 oder string2 NULL, ist das Ergebnis NULL.

    ```sql
    SELECT JARO_WINKLER('databend', NULL) AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │ NULL       │
    └────────────┘
    ```
- Leere Zeichenfolgen:
    - Der Vergleich zweier leerer Zeichenfolgen ergibt 1,0.

    ```sql
    SELECT JARO_WINKLER('', '') AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │          1 │
    └────────────┘
    ```
    - Der Vergleich einer leeren Zeichenfolge mit einer nicht leeren Zeichenfolge ergibt 0,0.

    ```sql
    SELECT JARO_WINKLER('databend', '') AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │          0 │
    └────────────┘
    ```
