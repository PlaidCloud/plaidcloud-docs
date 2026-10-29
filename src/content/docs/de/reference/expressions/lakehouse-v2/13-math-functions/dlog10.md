---
title: DLOG10 (Lakehouse v2)
description: DLOG10 – Alias für `LOG10`. Siehe [LOG10](../log10/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dlog10.md
---

Alias für `LOG10`. Siehe [LOG10](../log10/).

## Analyze-Syntax

```python
func.dlog10(1000)
```

## Analyze-Beispiele

```python
func.dlog10(1000)

┌─────┐
│ 3.0 │
└─────┘
```

## SQL-Syntax

```sql
DLOG10(<x>)
```

## SQL-Beispiele

```sql
SELECT DLOG10(1000);

┌─────┐
│ 3.0 │
└─────┘
```
