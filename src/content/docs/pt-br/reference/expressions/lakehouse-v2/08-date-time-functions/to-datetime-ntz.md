---
title: TO_DATETIME_NTZ (Lakehouse v2)
description: TO_DATETIME_NTZ — converte um valor em um DATETIME sem fuso horário (NTZ).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-datetime-ntz.md
---

Converte um valor em um DATETIME sem fuso horário (NTZ). O resultado não é afetado pelas configurações de fuso horário da sessão.

## Sintaxe do Analyze

```python
func.to_datetime_ntz('2024-06-15 14:30:00')
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT TO_DATETIME_NTZ('2024-06-15 14:30:00');

┌─────────────────────┐
│ 2024-06-15 14:30:00 │
└─────────────────────┘
```
