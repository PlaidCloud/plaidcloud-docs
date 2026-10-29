---
title: INSPECT_MV_RELATIONSHIPS (Lakehouse v2)
description: INSPECT_MV_RELATIONSHIPS — zwraca relacje zależności widoku zmaterializowanego.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-relationships.md
---

Zwraca relacje zależności widoku zmaterializowanego.

## Składnia Analyze

```python
func.inspect_mv_relationships(<db>, <mv>)
```

## Przykłady Analyze

```python
func.inspect_mv_relationships('mydb', 'my_mv')

┌─────────────────┐
│ (relationships)  │
└─────────────────┘
```

## Składnia SQL

```sql
INSPECT_MV_RELATIONSHIPS(<db>, <mv>)
```

## Przykłady SQL

```sql
SELECT * FROM TABLE(INSPECT_MV_RELATIONSHIPS('mydb', 'my_mv'));

┌─────────────────┐
│ (relationships)  │
└─────────────────┘
```
