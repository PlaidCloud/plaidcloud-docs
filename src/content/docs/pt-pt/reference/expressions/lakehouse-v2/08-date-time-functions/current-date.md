---
title: CURRENT_DATE (Lakehouse v2)
description: CURRENT_DATE — devolve a data atual. Alias de `CURDATE`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-date.md
---

Devolve a data atual. Alias de `CURDATE`.

## Sintaxe do Analyze

```python
func.current_date()
```

## Exemplos do Analyze

```python
func.current_date()

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Sintaxe SQL

```sql
CURRENT_DATE()
```

## Exemplos SQL

```sql
SELECT CURRENT_DATE();

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
