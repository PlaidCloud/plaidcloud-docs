---
title: "CAST, :: (Lakehouse v1)"
description: "CAST, :: – wandelt einen Wert von einem Datentyp in einen anderen um."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/cast.md
---

Wandelt einen Wert von einem Datentyp in einen anderen um. `::` ist ein Alias für CAST.

Siehe auch: [TRY_CAST](../try-cast)

## Analyze-Syntax

```python
func.cast( <expr>, <data_type> )
```

## Analyze-Beispiele

```python
func.cast(1, string), func.to_string(1)

┌───────────────────────────────────────────┐
│ func.cast(1, string) │ func.to_string(1)  │
├──────────────────────┼────────────────────┤
│ 1                    │ 1                  │
└───────────────────────────────────────────┘
```

## SQL-Syntax

```sql
CAST( <expr> AS <data_type> )

<expr>::<data_type>
```

## SQL-Beispiele

```sql
SELECT CAST(1 AS VARCHAR), 1::VARCHAR;

┌───────────────────────────────┐
│ cast(1 as string) │ 1::string │
├───────────────────┼───────────┤
│ 1                 │ 1         │
└───────────────────────────────┘
```
