---
title: TIMESTAMPDIFF (Lakehouse v2)
description: TIMESTAMPDIFF — retorna a diferença entre duas datas e horas na unidade especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timestampdiff.md
---

Retorna a diferença entre duas datas e horas na unidade especificada.

## Sintaxe do Analyze

```python
func.timestampdiff(<unit>, <start>, <end>)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT TIMESTAMPDIFF(DAY, '2024-01-01', '2024-03-01');

┌────┐
│ 60  │
└────┘
```
