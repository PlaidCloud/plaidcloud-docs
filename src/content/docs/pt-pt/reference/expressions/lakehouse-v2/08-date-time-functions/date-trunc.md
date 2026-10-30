---
title: DATE_TRUNC (Lakehouse v2)
description: DATE_TRUNC — trunca um valor de data ou data e hora para a precisão especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-trunc.md
---

Trunca um valor de data ou data e hora para a precisão especificada.

## Sintaxe do Analyze

```python
func.date_trunc(<unit>, <datetime>)
```

## Exemplos do Analyze

```python
func.date_trunc('MONTH', '2024-06-15')

┌──────────────┐
│ '2024-06-01'  │
└──────────────┘
```

## Sintaxe SQL

```sql
DATE_TRUNC(<unit>, <datetime>)
```

## Exemplos SQL

```sql
SELECT DATE_TRUNC('MONTH', '2024-06-15');

┌────────────┐
│ 2024-06-01  │
└────────────┘
```
