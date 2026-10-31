---
title: H3_TO_PARENT (Lakehouse v1)
description: H3_TO_PARENT — gibt den übergeordneten Index zurück, der h3 bei der Auflösung parent_res enthält.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-to-parent.md
---

Gibt den übergeordneten Index zurück, der `h3` bei der Auflösung `parent_res` enthält. Der Rückgabewert 0 bedeutet, dass ein Fehler aufgetreten ist.

## Analyze-Syntax

```python
func.h3_to_parent(h3, parent_res)
```

## Analyze-Beispiele

```python
func.h3_to_parent(635318325446452991, 12)

┌───────────────────────────────────────────┐
│ func.h3_to_parent(635318325446452991, 12) │
├───────────────────────────────────────────┤
│                        630814725819082751 │
└───────────────────────────────────────────┘
```

## SQL-Syntax

```sql
H3_TO_PARENT(h3, parent_res)
```

## SQL-Beispiele

```sql
SELECT H3_TO_PARENT(635318325446452991, 12);

┌──────────────────────────────────────┐
│ h3_to_parent(635318325446452991, 12) │
├──────────────────────────────────────┤
│                   630814725819082751 │
└──────────────────────────────────────┘
```
