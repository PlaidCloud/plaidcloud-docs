---
title: DATE (Lakehouse v2)
description: DATE — extrai a parte de data de uma expressão datetime.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date.md
---

Extrai a parte de data de uma expressão datetime.

## Sintaxe do Analyze

```python
func.date(<datetime>)
```

## Exemplos do Analyze

```python
func.date('2024-06-15 14:30:00')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Sintaxe SQL

```sql
DATE(<datetime>)
```

## Exemplos SQL

```sql
SELECT DATE('2024-06-15 14:30:00');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
