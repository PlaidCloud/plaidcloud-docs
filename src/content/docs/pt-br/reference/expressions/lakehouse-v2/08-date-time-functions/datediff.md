---
title: DATEDIFF (Lakehouse v2)
description: DATEDIFF — retorna o número de dias entre duas datas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/datediff.md
---

Retorna o número de dias entre duas datas.

## Sintaxe do Analyze

```python
func.datediff(<end_date>, <start_date>)
```

## Exemplos do Analyze

```python
func.datediff('2024-03-01', '2024-01-01')

┌────┐
│ 60  │
└────┘
```

## Sintaxe SQL

```sql
DATEDIFF(<end_date>, <start_date>)
```

## Exemplos SQL

```sql
SELECT DATEDIFF('2024-03-01', '2024-01-01');

┌────┐
│ 60  │
└────┘
```
