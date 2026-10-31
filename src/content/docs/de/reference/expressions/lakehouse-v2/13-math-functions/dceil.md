---
title: DCEIL (Lakehouse v2)
description: DCEIL – Alias für `CEIL`. Siehe [CEIL](../ceil/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dceil.md
---

Alias für `CEIL`. Siehe [CEIL](../ceil/).

## Analyze-Syntax

```python
func.dceil(3.2)
```

## Analyze-Beispiele

```python
func.dceil(3.2)

┌───┐
│ 4 │
└───┘
```

## SQL-Syntax

```sql
DCEIL(<x>)
```

## SQL-Beispiele

```sql
SELECT DCEIL(3.2);

┌───┐
│ 4 │
└───┘
```
