---
title: BITXOR (Lakehouse v2)
description: BITXOR – gibt das bitweise XOR zweier numerischer Werte zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitxor.md
---

Gibt das bitweise XOR zweier numerischer Werte zurück.

## Analyze-Syntax

```python
func.bitxor(<x>, <y>)
```

## Analyze-Beispiele

```python
func.bitxor(12, 10)

┌───┐
│ 6  │
└───┘
```

## SQL-Syntax

```sql
BITXOR(<x>, <y>)
```

## SQL-Beispiele

```sql
SELECT BITXOR(12, 10);

┌───┐
│ 6  │
└───┘
```
