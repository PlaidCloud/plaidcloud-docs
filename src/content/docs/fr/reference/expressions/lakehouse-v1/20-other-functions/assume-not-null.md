---
title: ASSUME_NOT_NULL (Lakehouse v1)
description: ASSUME_NOT_NULL — produit une valeur équivalente non Nullable à partir d'un type Nullable.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/assume-not-null.md
---

Produit une valeur équivalente non `Nullable` à partir d'un type Nullable. Si la valeur d'origine est `NULL`, le résultat est indéterminé. 

## Syntaxe Analyze

```python
func.assume_not_null(<x>)
```

## Exemples Analyze

```python
With a table like:

┌────────────────────┐
│        x  │   y    │
├────────────────────┤
│         1 │   NULL │
│         2 │      3 │
└────────────────────┘

func.assume_not_null(y)
┌─────────────────────────┐
│ func.assume_not_null(y) │
├─────────────────────────┤
│                       0 │
│                       3 │
└─────────────────────────┘
```

## Syntaxe SQL

```sql
ASSUME_NOT_NULL(<x>)
```

## Alias

- [REMOVE_NULLABLE](../remove-nullable)

## Type de retour

Renvoie le type de données d'origine pour un type non `Nullable` ; renvoie le type de données non `Nullable` sous-jacent pour un type `Nullable`.

## Exemples SQL

```sql
CREATE TABLE default.t_null ( x int,  y int null);

INSERT INTO default.t_null values (1, null), (2, 3);

SELECT ASSUME_NOT_NULL(y), REMOVE_NULLABLE(y) FROM t_null;

┌─────────────────────────────────────────┐
│ assume_not_null(y) │ remove_nullable(y) │
├────────────────────┼────────────────────┤
│                  0 │                  0 │
│                  3 │                  3 │
└─────────────────────────────────────────┘
```
