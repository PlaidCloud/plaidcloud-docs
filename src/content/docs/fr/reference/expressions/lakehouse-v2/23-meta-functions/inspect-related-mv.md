---
title: INSPECT_RELATED_MV (Lakehouse v2)
description: INSPECT_RELATED_MV — renvoie les vues matérialisées associées à une table.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-related-mv.md
---

Renvoie les vues matérialisées associées à une table.

## Syntaxe Analyze

```python
func.inspect_related_mv(<db>, <table>)
```

## Exemples Analyze

```python
func.inspect_related_mv('mydb', 'my_table')

┌───────────────┐
│ (related mvs)  │
└───────────────┘
```

## Syntaxe SQL

```sql
INSPECT_RELATED_MV(<db>, <table>)
```

## Exemples SQL

```sql
SELECT * FROM TABLE(INSPECT_RELATED_MV('mydb', 'my_table'));

┌───────────────┐
│ (related mvs)  │
└───────────────┘
```
