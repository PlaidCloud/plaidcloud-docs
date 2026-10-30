---
title: "CAST, :: (Lakehouse v1)"
description: "CAST, :: — konwertuje wartość z jednego typu danych na inny."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/cast.md
---

Konwertuje wartość z jednego typu danych na inny. `::` jest aliasem CAST.

Zobacz także: [TRY_CAST](../try-cast)

## Składnia Analyze

```python
func.cast( <expr>, <data_type> )
```

## Przykłady Analyze

```python
func.cast(1, string), func.to_string(1)

┌───────────────────────────────────────────┐
│ func.cast(1, string) │ func.to_string(1)  │
├──────────────────────┼────────────────────┤
│ 1                    │ 1                  │
└───────────────────────────────────────────┘
```

## Składnia SQL

```sql
CAST( <expr> AS <data_type> )

<expr>::<data_type>
```

## Przykłady SQL

```sql
SELECT CAST(1 AS VARCHAR), 1::VARCHAR;

┌───────────────────────────────┐
│ cast(1 as string) │ 1::string │
├───────────────────┼───────────┤
│ 1                 │ 1         │
└───────────────────────────────┘
```
