---
title: ATAN (Lakehouse v2)
description: ATAN – gibt den Arkustangens einer Zahl im Bogenmaß zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/atan.md
---

Gibt den Arkustangens einer Zahl im Bogenmaß zurück.

## Analyze-Syntax

```python
func.atan(<x>)
```

## Analyze-Beispiele

```python
func.atan(1)

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```

## SQL-Syntax

```sql
ATAN(<x>)
```

## SQL-Beispiele

```sql
SELECT ATAN(1);

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```
