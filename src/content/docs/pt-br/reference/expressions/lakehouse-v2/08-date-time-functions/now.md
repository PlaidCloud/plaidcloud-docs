---
title: NOW (Lakehouse v2)
description: NOW — retorna a data e a hora atuais.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/now.md
---

Retorna a data e a hora atuais.

## Sintaxe do Analyze

```python
func.now()
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT NOW();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
