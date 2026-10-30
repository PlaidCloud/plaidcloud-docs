---
title: TO_TERA_TIMESTAMP (Lakehouse v2)
description: "Utilize a função de data/hora TO_TERA_TIMESTAMP no PlaidCloud Lakehouse. Converte um valor VARCHAR num valor DATETIME de acordo com uma cadeia de formato Teradata."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-tera-timestamp.md
---

Converte um valor VARCHAR num valor DATETIME de acordo com uma cadeia de formato Teradata.

## Sintaxe de Analyze

```python
func.to_tera_timestamp(<str>, <format>)
```

## Exemplos de Analyze

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

## Exemplos SQL

```sql
SELECT TO_TERA_TIMESTAMP('20240615143000', 'YYYYMMDDHH24MISS');

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
