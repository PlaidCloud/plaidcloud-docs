---
title: INSPECT_MV_RELATIONSHIPS (Lakehouse v2)
description: INSPECT_MV_RELATIONSHIPS — gibt die Abhängigkeitsbeziehungen einer materialisierten Ansicht zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-relationships.md
---

Gibt die Abhängigkeitsbeziehungen einer materialisierten Ansicht zurück.

## Analyze-Syntax

```python
func.inspect_mv_relationships(<db>, <mv>)
```

## Analyze-Beispiele

```python
func.inspect_mv_relationships('mydb', 'my_mv')

┌─────────────────┐
│ (relationships)  │
└─────────────────┘
```

## SQL-Syntax

```sql
INSPECT_MV_RELATIONSHIPS(<db>, <mv>)
```

## SQL-Beispiele

```sql
SELECT * FROM TABLE(INSPECT_MV_RELATIONSHIPS('mydb', 'my_mv'));

┌─────────────────┐
│ (relationships)  │
└─────────────────┘
```
