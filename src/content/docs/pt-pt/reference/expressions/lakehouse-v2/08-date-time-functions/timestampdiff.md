---
title: TIMESTAMPDIFF (Lakehouse v2)
description: TIMESTAMPDIFF — devolve a diferença entre dois datetimes na unidade especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timestampdiff.md
---

Devolve a diferença entre dois datetimes na unidade especificada.

## Sintaxe de Analyze

```python
func.timestampdiff(<unit>, <start>, <end>)
```

## Exemplos de Analyze

```python
func.timestampdiff('DAY', '2024-01-01', '2024-03-01')

┌────┐
│ 60  │
└────┘
```

## Sintaxe SQL

```sql
TIMESTAMPDIFF(<unit>, <start>, <end>)
```

## Exemplos SQL

```sql
SELECT TIMESTAMPDIFF(DAY, '2024-01-01', '2024-03-01');

┌────┐
│ 60  │
└────┘
```
