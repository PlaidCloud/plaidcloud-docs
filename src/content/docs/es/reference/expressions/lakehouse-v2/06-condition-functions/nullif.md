---
title: NULLIF (Lakehouse v2)
description: NULLIF — devuelve NULL si dos expresiones son iguales; de lo contrario, devuelve la primera expresión.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/nullif.md
---

Devuelve NULL si dos expresiones son iguales; de lo contrario, devuelve la primera expresión.

## Sintaxis de Analyze

```python
func.nullif(get_column(table, 'value'), 0)
```

## Ejemplos de Analyze

```python
func.nullif(get_column(table, 'divisor'), 0)
```

## Sintaxis de SQL

```sql
NULLIF(<value>, 0)
```

## Ejemplos de SQL

```sql
SELECT 100 / NULLIF(divisor, 0) AS safe_division FROM calculations;

┌───────────────┐
│ safe_division │
├───────────────┤
│         50.00 │
│          NULL │
│         25.00 │
└───────────────┘
```
