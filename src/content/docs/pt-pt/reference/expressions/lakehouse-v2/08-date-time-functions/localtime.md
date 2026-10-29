---
title: LOCALTIME (Lakehouse v2)
description: LOCALTIME — devolve a data e hora atuais. Alias de `NOW`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/localtime.md
---

Devolve a data e hora atuais. Alias de `NOW`.

## Sintaxe do Analyze

```python
func.localtime()
```

## Exemplos do Analyze

```python
func.localtime()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## Sintaxe SQL

```sql
LOCALTIME()
```

## Exemplos SQL

```sql
SELECT LOCALTIME();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
