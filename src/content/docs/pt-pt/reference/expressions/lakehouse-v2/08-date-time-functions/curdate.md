---
title: CURDATE (Lakehouse v2)
description: CURDATE — devolve a data atual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/curdate.md
---

Devolve a data atual.

## Sintaxe do Analyze

```python
func.curdate()
```

## Exemplos do Analyze

```python
func.curdate()

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Sintaxe SQL

```sql
CURDATE()
```

## Exemplos SQL

```sql
SELECT CURDATE();

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
