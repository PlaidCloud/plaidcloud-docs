---
title: FROM_UNIXTIME (Lakehouse v2)
description: FROM_UNIXTIME — converte um carimbo de data/hora Unix numa cadeia de data e hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/from-unixtime.md
---

Converte um carimbo de data/hora Unix numa cadeia de data e hora.

## Sintaxe do Analyze

```python
func.from_unixtime(<timestamp>[, <format>])
```

## Exemplos do Analyze

```python
func.from_unixtime(1704067200)

┌───────────────────────┐
│ '2024-01-01 00:00:00'  │
└───────────────────────┘
```

## Sintaxe SQL

```sql
FROM_UNIXTIME(<timestamp>[, <format>])
```

## Exemplos SQL

```sql
SELECT FROM_UNIXTIME(1704067200);

┌─────────────────────┐
│ 2024-01-01 00:00:00  │
└─────────────────────┘
```
