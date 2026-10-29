---
title: "CAST, :: (Lakehouse v1)"
description: "CAST, :: — convierte un valor de un tipo de datos a otro."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/cast.md
---

Convierte un valor de un tipo de datos a otro. `::` es un alias de CAST.

Consulte también: [TRY_CAST](../try-cast)

## Sintaxis de Analyze

```python
func.cast( <expr>, <data_type> )
```

## Ejemplos de Analyze

```python
func.cast(1, string), func.to_string(1)

┌───────────────────────────────────────────┐
│ func.cast(1, string) │ func.to_string(1)  │
├──────────────────────┼────────────────────┤
│ 1                    │ 1                  │
└───────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
CAST( <expr> AS <data_type> )

<expr>::<data_type>
```

## Ejemplos de SQL

```sql
SELECT CAST(1 AS VARCHAR), 1::VARCHAR;

┌───────────────────────────────┐
│ cast(1 as string) │ 1::string │
├───────────────────┼───────────┤
│ 1                 │ 1         │
└───────────────────────────────┘
```
