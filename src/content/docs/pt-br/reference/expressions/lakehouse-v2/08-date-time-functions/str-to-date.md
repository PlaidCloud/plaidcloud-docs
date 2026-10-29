---
title: STR_TO_DATE (Lakehouse v2)
description: STR_TO_DATE — converte uma string em uma data usando uma string de formato.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/str-to-date.md
---

Converte uma string em uma data usando uma string de formato.

## Sintaxe do Analyze

```python
func.str_to_date(<str>, <format>)
```

## Exemplos do Analyze

```python
func.str_to_date('Jun 15 2024', '%b %d %Y')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Sintaxe SQL

```sql
STR_TO_DATE(<str>, <format>)
```

## Exemplos de SQL

```sql
SELECT STR_TO_DATE('Jun 15 2024', '%b %d %Y');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
