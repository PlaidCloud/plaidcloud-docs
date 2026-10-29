---
title: TRY_CAST (Lakehouse v1)
description: TRY_CAST – wandelt einen Wert von einem Datentyp in einen anderen um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/try-cast.md
---

Wandelt einen Wert von einem Datentyp in einen anderen um. Gibt bei einem Fehler NULL zurück.

Siehe auch: [CAST](../cast)

## Analyze-Syntax

```python
func.try_cast( <expr>, <data_type> )
```

## Analyze-Beispiele

```python
func.try_cast(1, string)

┌──────────────────────────┐
│ func.try_cast(1, string) │
├──────────────────────────┤
│ 1                        │
└──────────────────────────┘
```

## SQL-Syntax

```sql
TRY_CAST( <expr> AS <data_type> )
```

## SQL-Beispiele

```sql
SELECT TRY_CAST(1 AS VARCHAR);

┌───────────────────────┐
│ try_cast(1 as string) │
├───────────────────────┤
│ 1                     │
└───────────────────────┘
```
