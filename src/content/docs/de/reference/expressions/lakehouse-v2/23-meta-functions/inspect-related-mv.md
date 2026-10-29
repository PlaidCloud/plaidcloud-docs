---
title: INSPECT_RELATED_MV (Lakehouse v2)
description: INSPECT_RELATED_MV — Gibt die zu einer Tabelle gehörenden materialisierten Ansichten zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-related-mv.md
---

Gibt die zu einer Tabelle gehörenden materialisierten Ansichten zurück.

## Analyze-Syntax

```python
func.inspect_related_mv(<db>, <table>)
```

## Analyze-Beispiele

```python
func.inspect_related_mv('mydb', 'my_table')

┌───────────────┐
│ (related mvs)  │
└───────────────┘
```

## SQL-Syntax

```sql
INSPECT_RELATED_MV(<db>, <table>)
```

## SQL-Beispiele

```sql
SELECT * FROM TABLE(INSPECT_RELATED_MV('mydb', 'my_table'));

┌───────────────┐
│ (related mvs)  │
└───────────────┘
```
