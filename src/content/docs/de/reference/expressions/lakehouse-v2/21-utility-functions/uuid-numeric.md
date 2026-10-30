---
title: UUID_NUMERIC (Lakehouse v2)
description: UUID_NUMERIC — Gibt eine zufällige UUID als 128-Bit-LARGEINT-Wert zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid-numeric.md
---

Gibt eine zufällige UUID als 128-Bit-LARGEINT-Wert zurück.

## Analyze-Syntax

```python
func.uuid_numeric()
```

## Analyze-Beispiele

```python
func.uuid_numeric()

┌────────────┐
│ (largeint)  │
└────────────┘
```

## SQL-Syntax

```sql
UUID_NUMERIC()
```

## SQL-Beispiele

```sql
SELECT UUID_NUMERIC();

┌─────────────────────────────────────────┐
│ 113304629137197850819971302868472922876  │
└─────────────────────────────────────────┘
```
