---
title: INSPECT_RELATED_MV (Lakehouse v2)
description: INSPECT_RELATED_MV — zwraca widoki zmaterializowane powiązane z tabelą.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-related-mv.md
---

Zwraca widoki zmaterializowane powiązane z tabelą.

## Składnia Analyze

```python
func.inspect_related_mv(<db>, <table>)
```

## Przykłady Analyze

```python
func.inspect_related_mv('mydb', 'my_table')

┌───────────────┐
│ (related mvs)  │
└───────────────┘
```

## Składnia SQL

```sql
INSPECT_RELATED_MV(<db>, <table>)
```

## Przykłady SQL

```sql
SELECT * FROM TABLE(INSPECT_RELATED_MV('mydb', 'my_table'));

┌───────────────┐
│ (related mvs)  │
└───────────────┘
```
