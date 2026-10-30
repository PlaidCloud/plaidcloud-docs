---
title: UUID_V7_NUMERIC (Lakehouse v2)
description: UUID_V7_NUMERIC — gibt eine zeitlich geordnete UUID v7 als 128-Bit-LARGEINT-Wert zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid-v7-numeric.md
---

Gibt eine zeitlich geordnete UUID v7 als 128-Bit-LARGEINT-Wert zurück. UUID-v7-Werte lassen sich nach Erstellungszeitpunkt sortieren.

## Analyze-Syntax

```python
func.uuid_v7_numeric()
```

## Analyze-Beispiele

```python
func.uuid_v7_numeric()

┌────────────────────────────────────┐
│ 2049638230412545024000012345678901 │
└────────────────────────────────────┘
```

## SQL-Syntax

```sql
UUID_V7_NUMERIC()
```

## SQL-Beispiele

```sql
SELECT UUID_V7_NUMERIC();

┌────────────────────────────────────┐
│ 2049638230412545024000012345678901 │
└────────────────────────────────────┘
```
