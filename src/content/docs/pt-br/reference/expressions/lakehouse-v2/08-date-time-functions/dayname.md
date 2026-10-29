---
title: DAYNAME (Lakehouse v2)
description: DAYNAME — retorna o nome do dia da semana de uma data.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/dayname.md
---

Retorna o nome do dia da semana de uma data.

## Sintaxe do Analyze

```python
func.dayname(<date>)
```

## Exemplos do Analyze

```python
func.dayname('2024-06-15')

┌────────────┐
│ 'Saturday'  │
└────────────┘
```

## Sintaxe SQL

```sql
DAYNAME(<date>)
```

## Exemplos SQL

```sql
SELECT DAYNAME('2024-06-15');

┌──────────┐
│ Saturday  │
└──────────┘
```
