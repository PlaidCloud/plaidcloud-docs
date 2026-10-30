---
title: TRY_CAST (Lakehouse v1)
description: TRY_CAST — convierte un valor de un tipo de datos a otro.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/try-cast.md
---

Convierte un valor de un tipo de datos a otro. Devuelve NULL si se produce un error.

Consulte también: [CAST](../cast)

## Sintaxis de Analyze

```python
func.try_cast( <expr>, <data_type> )
```

## Ejemplos de Analyze

```python
func.try_cast(1, string)

┌──────────────────────────┐
│ func.try_cast(1, string) │
├──────────────────────────┤
│ 1                        │
└──────────────────────────┘
```

## Sintaxis de SQL

```sql
TRY_CAST( <expr> AS <data_type> )
```

## Ejemplos de SQL

```sql
SELECT TRY_CAST(1 AS VARCHAR);

┌───────────────────────┐
│ try_cast(1 as string) │
├───────────────────────┤
│ 1                     │
└───────────────────────┘
```
