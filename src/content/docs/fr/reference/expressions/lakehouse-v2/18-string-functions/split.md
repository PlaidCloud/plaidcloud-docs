---
title: SPLIT (Lakehouse v2)
description: SPLIT — découpe une chaîne selon un délimiteur et renvoie un tableau.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/split.md
---

Découpe une chaîne selon un délimiteur et renvoie un tableau.

## Syntaxe Analyze

```python
func.split(<str>, <delimiter>)
```

## Exemples Analyze

```python
func.split('a,b,c', ',')

┌───────────────┐
│ ['a','b','c']  │
└───────────────┘
```

## Syntaxe SQL

```sql
SPLIT(<str>, <delimiter>)
```

## Exemples SQL

```sql
SELECT SPLIT('a,b,c', ',');

┌───────────────┐
│ ["a","b","c"]  │
└───────────────┘
```
