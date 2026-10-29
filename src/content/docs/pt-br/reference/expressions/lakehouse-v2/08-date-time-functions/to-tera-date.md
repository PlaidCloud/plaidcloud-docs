---
title: TO_TERA_DATE (Lakehouse v2)
description: TO_TERA_DATE — converte um valor VARCHAR em um valor DATE de acordo com uma string de formato do Teradata.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-tera-date.md
---

Converte um valor VARCHAR em um valor DATE de acordo com uma string de formato do Teradata.

## Sintaxe do Analyze

```python
func.to_tera_date(<str>, <format>)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT TO_TERA_DATE('20240615', 'YYYYMMDD');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
