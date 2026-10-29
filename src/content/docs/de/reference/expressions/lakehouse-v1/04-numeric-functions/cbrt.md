---
title: CBRT (Lakehouse v1)
description: CBRT – gibt die Kubikwurzel einer nicht negativen Zahl x zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/cbrt.md
---

Gibt die Kubikwurzel einer nicht negativen Zahl `x` zurück.

## Analyze-Syntax

```python
func.cbrt( <x> )
```

## Analyze-Beispiele

```python
func.cbrt(27)

┌───────────────┐
│ func.cbrt(27) │
├───────────────┤
│             3 │
└───────────────┘
```

## SQL-Syntax

```sql
CBRT( <x> )
```

## SQL-Beispiele

```sql
SELECT CBRT(27);

┌──────────┐
│ cbrt(27) │
├──────────┤
│        3 │
└──────────┘
```
