---
title: CURRENT_WAREHOUSE (Lakehouse v2)
description: CURRENT_WAREHOUSE — Devuelve el nombre del almacén actual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/current-warehouse.md
---

Devuelve el nombre del almacén actual.

## Sintaxis de Analyze

```python
func.current_warehouse()
```

## Ejemplos de Analyze

```python
func.current_warehouse()

┌───────────────────┐
│ default_warehouse │
└───────────────────┘
```

## Sintaxis de SQL

```sql
CURRENT_WAREHOUSE()
```

## Ejemplos de SQL

```sql
SELECT CURRENT_WAREHOUSE();

┌───────────────────┐
│ default_warehouse │
└───────────────────┘
```
