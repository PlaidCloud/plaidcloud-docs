---
title: TO_DATE (Lakehouse v2)
description: TO_DATE — converte uma data e hora em uma data.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-date.md
---

Converte uma data e hora em uma data.

## Sintaxe do Analyze

```python
func.to_date(<datetime>)
```

## Exemplos do Analyze

```python
func.to_date('2024-06-15 14:30:00')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Sintaxe SQL

```sql
TO_DATE(<datetime>)
```

## Exemplos de SQL

```sql
SELECT TO_DATE('2024-06-15 14:30:00');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
