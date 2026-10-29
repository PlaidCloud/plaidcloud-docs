---
title: BIN (Lakehouse v2)
description: BIN – gibt die binäre Zeichenfolgendarstellung einer Ganzzahl zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/bin.md
---

Gibt die binäre Zeichenfolgendarstellung einer Ganzzahl zurück.

## Analyze-Syntax

```python
func.bin(<x>)
```

## Analyze-Beispiele

```python
func.bin(10)

┌────────┐
│ '1010'  │
└────────┘
```

## SQL-Syntax

```sql
BIN(<x>)
```

## SQL-Beispiele

```sql
SELECT BIN(10);

┌──────┐
│ 1010  │
└──────┘
```
