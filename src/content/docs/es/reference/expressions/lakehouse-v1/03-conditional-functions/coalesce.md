---
title: COALESCE (Lakehouse v1)
description: COALESCE — devuelve la primera expresión que no es NULL entre sus argumentos; si todos los argumentos son NULL, devuelve NULL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/coalesce.md
---

Devuelve la primera expresión que no es NULL entre sus argumentos; si todos los argumentos son NULL, devuelve NULL.

## Sintaxis de Analyze
```python
func.coalesce(<expr1>[, <expr2> ...])
```

## Ejemplos de Analyze

```sql
func.coalesce(table.UOM,  'none', \n)

func.coalesce(get_column(table2, 'TECHNOLOGY_RATE'), 0.0)

func.coalesce(table_beta.adjusted_price, table_alpha.override_price, table_alpha.price) * table_beta.quantity_sold
```

## Sintaxis de SQL

```sql
COALESCE(<expr1>[, <expr2> ...])
```

## Ejemplos de SQL

```sql
SELECT COALESCE(1), COALESCE(1, NULL), COALESCE(NULL, 1, 2);

┌────────────────────────────────────────────────────────┐
│ coalesce(1) │ coalesce(1, null) │ coalesce(null, 1, 2) │
├─────────────┼───────────────────┼──────────────────────┤
│           1 │                 1 │                    1 │
└────────────────────────────────────────────────────────┘

SELECT COALESCE('a'), COALESCE('a', NULL), COALESCE(NULL, 'a', 'b');

┌────────────────────────────────────────────────────────────────┐
│ coalesce('a') │ coalesce('a', null) │ coalesce(null, 'a', 'b') │
├───────────────┼─────────────────────┼──────────────────────────┤
│ a             │ a                   │ a                        │
└────────────────────────────────────────────────────────────────┘
```
