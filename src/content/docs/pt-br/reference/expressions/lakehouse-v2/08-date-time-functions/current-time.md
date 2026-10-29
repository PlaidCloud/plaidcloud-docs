---
title: CURRENT_TIME (Lakehouse v2)
description: CURRENT_TIME — retorna a hora atual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-time.md
---

Retorna a hora atual.

## Sintaxe do Analyze

```python
func.current_time()
```

## Exemplos do Analyze

```python
func.current_time()

┌────────────┐
│ '14:30:00'  │
└────────────┘
```

## Sintaxe SQL

```sql
CURRENT_TIME()
```

## Exemplos SQL

```sql
SELECT CURRENT_TIME();

┌──────────┐
│ 14:30:00  │
└──────────┘
```
