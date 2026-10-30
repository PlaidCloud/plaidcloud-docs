---
title: "ELEMENT_AT (Array, Lakehouse v2)"
description: ELEMENT_AT – gibt das Element an einer angegebenen Position in einem Array zurück (Zählung ab 1).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/element-at.md
---

Gibt das Element an einer angegebenen Position in einem Array zurück (Zählung ab 1).

## Analyze-Syntax

```python
func.element_at([10, 20, 30], 2)
```

## Analyze-Beispiele

```python
func.element_at([10, 20, 30], 2)

┌────┐
│ 20 │
└────┘
```

## SQL-Syntax

```sql
ELEMENT_AT([10, 20, 30], 2)
```

## SQL-Beispiele

```sql
SELECT ELEMENT_AT([10, 20, 30], 2);

┌────┐
│ 20 │
└────┘
```
