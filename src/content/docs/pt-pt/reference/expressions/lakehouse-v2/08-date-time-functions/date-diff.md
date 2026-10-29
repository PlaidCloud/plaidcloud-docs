---
title: DATE_DIFF (Lakehouse v2)
description: DATE_DIFF — devolve a diferença entre duas datas na unidade especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-diff.md
---

Devolve a diferença entre duas datas na unidade especificada.

## Sintaxe do Analyze

```python
func.date_diff(<unit>, <start>, <end>)
```

## Exemplos do Analyze

```python
func.date_diff('DAY', '2024-01-01', '2024-03-01')

┌────┐
│ 60  │
└────┘
```

## Sintaxe SQL

```sql
DATE_DIFF(<unit>, <start>, <end>)
```

## Exemplos SQL

```sql
SELECT DATE_DIFF('DAY', '2024-01-01', '2024-03-01');

┌────┐
│ 60  │
└────┘
```
