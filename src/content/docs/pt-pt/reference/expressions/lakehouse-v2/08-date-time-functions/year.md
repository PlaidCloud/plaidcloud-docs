---
title: YEAR (Lakehouse v2)
description: YEAR — devolve o ano de uma data.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/year.md
---

Devolve o ano de uma data.

## Sintaxe de Analyze

```python
func.year(<date>)
```

## Exemplos de Analyze

```python
func.year('2024-06-15')

┌──────┐
│ 2024  │
└──────┘
```

## Sintaxe SQL

```sql
YEAR(<date>)
```

## Exemplos SQL

```sql
SELECT YEAR('2024-06-15');

┌──────┐
│ 2024  │
└──────┘
```
