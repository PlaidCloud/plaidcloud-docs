---
title: LOCALTIMESTAMP (Lakehouse v2)
description: LOCALTIMESTAMP — retorna a data e a hora atuais. Alias de `NOW`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/localtimestamp.md
---

Retorna a data e a hora atuais. Alias de `NOW`.

## Sintaxe do Analyze

```python
func.localtimestamp()
```

## Exemplos do Analyze

```python
func.localtimestamp()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## Sintaxe SQL

```sql
LOCALTIMESTAMP()
```

## Exemplos SQL

```sql
SELECT LOCALTIMESTAMP();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
