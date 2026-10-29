---
title: TO_DATE (Lakehouse v2)
description: TO_DATE — converte um datetime numa data.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-date.md
---

Converte um datetime numa data.

## Sintaxe de Analyze

```python
func.to_date(<datetime>)
```

## Exemplos de Analyze

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

## Exemplos SQL

```sql
SELECT TO_DATE('2024-06-15 14:30:00');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
