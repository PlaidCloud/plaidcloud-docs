---
title: NOW (Lakehouse v2)
description: NOW — devolve a data e hora atuais.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/now.md
---

Devolve a data e hora atuais.

## Sintaxe de Analyze

```python
func.now()
```

## Exemplos de Analyze

```python
func.now()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## Sintaxe SQL

```sql
NOW()
```

## Exemplos SQL

```sql
SELECT NOW();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
