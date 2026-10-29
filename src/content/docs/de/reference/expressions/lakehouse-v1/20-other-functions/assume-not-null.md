---
title: ASSUME_NOT_NULL (Lakehouse v1)
description: ASSUME_NOT_NULL liefert für einen Nullable-Typ einen äquivalenten Wert ohne Nullable.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/assume-not-null.md
---

Liefert für einen Nullable-Typ einen äquivalenten Wert ohne `Nullable`. Ist der ursprüngliche Wert `NULL`, ist das Ergebnis nicht definiert. 

## Analyze-Syntax

```python
func.assume_not_null(<x>)
```

## Analyze-Beispiele

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

## SQL-Syntax

```sql
ASSUME_NOT_NULL(<x>)
```

## Aliasse

- [REMOVE_NULLABLE](../remove-nullable)

## Rückgabetyp

Gibt für einen Typ ohne `Nullable` den ursprünglichen Datentyp zurück. Für einen `Nullable`-Typ wird der eingebettete Datentyp ohne `Nullable` zurückgegeben.

## SQL-Beispiele

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
