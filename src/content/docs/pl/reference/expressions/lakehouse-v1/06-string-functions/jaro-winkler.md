---
title: JARO_WINKLER (Lakehouse v1)
description: JARO_WINKLER — oblicza odległość Jaro-Winklera między dwoma ciągami znaków.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/jaro-winkler.md
---

Oblicza [odległość Jaro-Winklera](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance) między dwoma ciągami znaków. Jest powszechnie używana do pomiaru podobieństwa ciągów, a jej wartości mieszczą się w zakresie od 0,0 (całkowicie różne) do 1,0 (identyczne ciągi). 

## Składnia Analyze

```python
func.jaro_winkler(<string1>, <string2>)
```

## Przykłady Analyze

```python
func.jaro_winkler('databend', 'Databend')
┌───────────────────────────────────────────┐
│ func.jaro_winkler('databend', 'Databend') │
├───────────────────────────────────────────┤
│                        0.9166666666666666 │
└───────────────────────────────────────────┘
```

## Składnia SQL

```sql
JARO_WINKLER(<string1>, <string2>)
```

## Przykłady SQL

Funkcja JARO_WINKLER zwraca wartość FLOAT64 określającą podobieństwo między dwoma ciągami wejściowymi. Zwracana wartość podlega następującym regułom:

- Zakres podobieństwa: wynik mieści się w zakresie od 0,0 (całkowicie różne) do 1,0 (identyczne).

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
- Obsługa wartości NULL: jeśli string1 lub string2 ma wartość NULL, wynikiem jest NULL.

    ```sql
    SELECT JARO_WINKLER('databend', NULL) AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │ NULL       │
    └────────────┘
    ```
- Puste ciągi znaków:
    - Porównanie dwóch pustych ciągów zwraca 1,0.

    ```sql
    SELECT JARO_WINKLER('', '') AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │          1 │
    └────────────┘
    ```
    - Porównanie pustego ciągu z niepustym zwraca 0,0.

    ```sql
    SELECT JARO_WINKLER('databend', '') AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │          0 │
    └────────────┘
    ```
