---
title: TO_TERA_DATE (Lakehouse v2)
description: TO_TERA_DATE — converte um valor VARCHAR num valor DATE de acordo com uma cadeia de formato Teradata.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-tera-date.md
---

Converte um valor VARCHAR num valor DATE de acordo com uma cadeia de formato Teradata.

## Sintaxe de Analyze

```python
func.to_tera_date(<str>, <format>)
```

## Exemplos de Analyze

```python
func.to_tera_date('20240615', 'YYYYMMDD')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Sintaxe SQL

```sql
TO_TERA_DATE(<str>, <format>)
```

## Exemplos SQL

```sql
SELECT TO_TERA_DATE('20240615', 'YYYYMMDD');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
