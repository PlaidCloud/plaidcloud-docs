---
title: JARO_WINKLER (Lakehouse v1)
description: JARO_WINKLER calcule la distance de Jaro-Winkler entre deux chaînes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/jaro-winkler.md
---

Calcule la [distance de Jaro-Winkler](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance) entre deux chaînes. Elle sert couramment à mesurer la similarité entre des chaînes, avec des valeurs allant de 0.0 (totalement différentes) à 1.0 (chaînes identiques). 

## Syntaxe Analyze

```python
func.jaro_winkler(<string1>, <string2>)
```

## Exemples Analyze

```python
func.jaro_winkler('databend', 'Databend')
┌───────────────────────────────────────────┐
│ func.jaro_winkler('databend', 'Databend') │
├───────────────────────────────────────────┤
│                        0.9166666666666666 │
└───────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
JARO_WINKLER(<string1>, <string2>)
```

## Exemples SQL

La fonction JARO_WINKLER renvoie une valeur FLOAT64 représentant la similarité entre les deux chaînes d'entrée. La valeur renvoyée obéit aux règles suivantes :

- Plage de similarité : le résultat va de 0.0 (totalement différentes) à 1.0 (identiques).

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
- Gestion de NULL : si string1 ou string2 est NULL, le résultat est NULL.

    ```sql
    SELECT JARO_WINKLER('databend', NULL) AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │ NULL       │
    └────────────┘
    ```
- Chaînes vides :
    - La comparaison de deux chaînes vides renvoie 1.0.

    ```sql
    SELECT JARO_WINKLER('', '') AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │          1 │
    └────────────┘
    ```
    - La comparaison d'une chaîne vide avec une chaîne non vide renvoie 0.0.

    ```sql
    SELECT JARO_WINKLER('databend', '') AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │          0 │
    └────────────┘
    ```
