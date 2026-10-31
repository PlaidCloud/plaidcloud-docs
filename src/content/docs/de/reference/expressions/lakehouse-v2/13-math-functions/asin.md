---
title: ASIN (Lakehouse v2)
description: ASIN – gibt den Arkussinus einer Zahl im Bogenmaß zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/asin.md
---

Gibt den Arkussinus einer Zahl im Bogenmaß zurück.

## Analyze-Syntax

```python
func.asin(<x>)
```

## Analyze-Beispiele

```python
func.asin(0.5)

┌────────────────────┐
│ 0.5235987755982988  │
└────────────────────┘
```

## SQL-Syntax

```sql
ASIN(<x>)
```

## SQL-Beispiele

```sql
SELECT ASIN(0.5);

┌────────────────────┐
│ 0.5235987755982988  │
└────────────────────┘
```
