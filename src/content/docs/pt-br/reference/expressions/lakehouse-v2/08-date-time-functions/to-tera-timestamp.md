---
title: TO_TERA_TIMESTAMP (Lakehouse v2)
description: "Use a função de data e hora TO_TERA_TIMESTAMP no PlaidCloud Lakehouse. Converte um valor VARCHAR em um valor DATETIME de acordo com uma string de formato do Teradata."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-tera-timestamp.md
---

Converte um valor VARCHAR em um valor DATETIME de acordo com uma string de formato do Teradata.

## Sintaxe do Analyze

```python
func.to_tera_timestamp(<str>, <format>)
```

## Exemplos do Analyze

```python
func.to_tera_timestamp('20240615143000', 'YYYYMMDDHH24MISS')

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## Sintaxe SQL

```sql
TO_TERA_TIMESTAMP(<str>, <format>)
```

## Exemplos de SQL

```sql
SELECT TO_TERA_TIMESTAMP('20240615143000', 'YYYYMMDDHH24MISS');

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
