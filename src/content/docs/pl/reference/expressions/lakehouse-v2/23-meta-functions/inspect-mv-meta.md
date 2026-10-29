---
title: INSPECT_MV_META (Lakehouse v2)
description: INSPECT_MV_META — zwraca metadane widoku zmaterializowanego.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-meta.md
---

Zwraca metadane widoku zmaterializowanego.

## Składnia Analyze

```python
func.inspect_mv_meta(<db>, <mv>)
```

## Przykłady Analyze

```python
func.inspect_mv_meta('mydb', 'my_mv')

┌───────────────┐
│ (mv metadata)  │
└───────────────┘
```

## Składnia SQL

```sql
INSPECT_MV_META(<db>, <mv>)
```

## Przykłady SQL

```sql
SELECT * FROM TABLE(INSPECT_MV_META('mydb', 'my_mv'));

┌───────────────┐
│ (mv metadata)  │
└───────────────┘
```
