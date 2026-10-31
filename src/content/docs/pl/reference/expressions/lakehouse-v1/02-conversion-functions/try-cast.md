---
title: TRY_CAST (Lakehouse v1)
description: TRY_CAST — konwertuje wartość z jednego typu danych na inny.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/try-cast.md
---

Konwertuje wartość z jednego typu danych na inny. W razie błędu zwraca NULL.

Zobacz także: [CAST](../cast)

## Składnia Analyze

```python
func.try_cast( <expr>, <data_type> )
```

## Przykłady Analyze

```python
func.try_cast(1, string)

┌──────────────────────────┐
│ func.try_cast(1, string) │
├──────────────────────────┤
│ 1                        │
└──────────────────────────┘
```

## Składnia SQL

```sql
TRY_CAST( <expr> AS <data_type> )
```

## Przykłady SQL

```sql
SELECT TRY_CAST(1 AS VARCHAR);

┌───────────────────────┐
│ try_cast(1 as string) │
├───────────────────────┤
│ 1                     │
└───────────────────────┘
```
