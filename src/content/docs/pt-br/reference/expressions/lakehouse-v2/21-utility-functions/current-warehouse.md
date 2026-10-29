---
title: CURRENT_WAREHOUSE (Lakehouse v2)
description: CURRENT_WAREHOUSE — Retorna o nome do armazém atual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/current-warehouse.md
---

Retorna o nome do armazém atual.

## Sintaxe do Analyze

```python
func.current_warehouse()
```

## Exemplos do Analyze

```python
func.current_warehouse()

┌───────────────────┐
│ default_warehouse │
└───────────────────┘
```

## Sintaxe SQL

```sql
CURRENT_WAREHOUSE()
```

## Exemplos de SQL

```sql
SELECT CURRENT_WAREHOUSE();

┌───────────────────┐
│ default_warehouse │
└───────────────────┘
```
