---
title: MAKEDATE (Lakehouse v2)
description: MAKEDATE — crea una fecha a partir de un año y un valor de día del año.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/makedate.md
---

Crea una fecha a partir de un año y un valor de día del año.

## Sintaxis de Analyze

```python
func.makedate(<year>, <dayofyear>)
```

## Ejemplos de Analyze

```python
func.makedate(2024, 100)

┌──────────────┐
│ '2024-04-09'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
MAKEDATE(<year>, <dayofyear>)
```

## Ejemplos de SQL

```sql
SELECT MAKEDATE(2024, 100);

┌────────────┐
│ 2024-04-09  │
└────────────┘
```
