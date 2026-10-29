---
title: DIVIDE (Lakehouse v2)
description: DIVIDE – gibt das Ergebnis der Division einer Zahl durch eine andere zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/divide.md
---

Gibt das Ergebnis der Division einer Zahl durch eine andere zurück.

## Analyze-Syntax

```python
func.divide(<x>, <y>)
```

## Analyze-Beispiele

```python
func.divide(10, 3)

┌────────────────────┐
│ 3.3333333333333335  │
└────────────────────┘
```

## SQL-Syntax

```sql
DIVIDE(<x>, <y>)
```

## SQL-Beispiele

```sql
SELECT DIVIDE(10, 3);

┌────────────────────┐
│ 3.3333333333333335  │
└────────────────────┘
```
