---
title: INSPECT_MV_META (Lakehouse v2)
description: INSPECT_MV_META — gibt Metadaten zu einer materialisierten Ansicht zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-meta.md
---

Gibt Metadaten zu einer materialisierten Ansicht zurück.

## Analyze-Syntax

```python
func.inspect_mv_meta(<db>, <mv>)
```

## Analyze-Beispiele

```python
func.inspect_mv_meta('mydb', 'my_mv')

┌───────────────┐
│ (mv metadata)  │
└───────────────┘
```

## SQL-Syntax

```sql
INSPECT_MV_META(<db>, <mv>)
```

## SQL-Beispiele

```sql
SELECT * FROM TABLE(INSPECT_MV_META('mydb', 'my_mv'));

┌───────────────┐
│ (mv metadata)  │
└───────────────┘
```
