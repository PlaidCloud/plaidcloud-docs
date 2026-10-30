---
title: TO_DATETIME_NTZ (Lakehouse v2)
description: TO_DATETIME_NTZ — converte um valor num DATETIME sem fuso horário (NTZ).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-datetime-ntz.md
---

Converte um valor num DATETIME sem fuso horário (NTZ). O resultado não é afetado pelas definições de fuso horário da sessão.

## Sintaxe de Analyze

```python
func.to_datetime_ntz('2024-06-15 14:30:00')
```

## Exemplos de Analyze

```python
func.to_datetime_ntz('2024-06-15 14:30:00')

┌─────────────────────┐
│ 2024-06-15 14:30:00 │
└─────────────────────┘
```

## Sintaxe SQL

```sql
TO_DATETIME_NTZ(<expr>)
```

## Exemplos SQL

```sql
SELECT TO_DATETIME_NTZ('2024-06-15 14:30:00');

┌─────────────────────┐
│ 2024-06-15 14:30:00 │
└─────────────────────┘
```
