---
title: TIMESTAMPDIFF (Lakehouse v2)
description: TIMESTAMPDIFF — devuelve la diferencia entre dos valores de fecha y hora en la unidad especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timestampdiff.md
---

Devuelve la diferencia entre dos valores de fecha y hora en la unidad especificada.

## Sintaxis de Analyze

```python
func.timestampdiff(<unit>, <start>, <end>)
```

## Ejemplos de Analyze

```python
func.timestampdiff('DAY', '2024-01-01', '2024-03-01')

┌────┐
│ 60  │
└────┘
```

## Sintaxis de SQL

```sql
TIMESTAMPDIFF(<unit>, <start>, <end>)
```

## Ejemplos de SQL

```sql
SELECT TIMESTAMPDIFF(DAY, '2024-01-01', '2024-03-01');

┌────┐
│ 60  │
└────┘
```
