---
title: TRUNCATE (Lakehouse v2)
description: TRUNCATE – schneidet eine Zahl auf eine angegebene Anzahl von Dezimalstellen ab.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/truncate.md
---

Schneidet eine Zahl auf eine angegebene Anzahl von Dezimalstellen ab.

## Analyze-Syntax

```python
func.truncate(<x>, <d>)
```

## Analyze-Beispiele

```python
func.truncate(3.14159, 2)

┌──────┐
│ 3.14  │
└──────┘
```

## SQL-Syntax

```sql
TRUNCATE(<x>, <d>)
```

## SQL-Beispiele

```sql
SELECT TRUNCATE(3.14159, 2);

┌──────┐
│ 3.14  │
└──────┘
```
