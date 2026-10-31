---
title: SPLIT_PART (Lakehouse v2)
description: SPLIT_PART — découpe une chaîne selon un délimiteur et renvoie l'élément situé à un indice donné.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/split-part.md
---

Découpe une chaîne selon un délimiteur et renvoie l'élément situé à un indice donné.

## Syntaxe Analyze

```python
func.split_part(<str>, <delimiter>, <index>)
```

## Exemples Analyze

```python
func.split_part('a-b-c', '-', 2)

┌─────┐
│ 'b'  │
└─────┘
```

## Syntaxe SQL

```sql
SPLIT_PART(<str>, <delimiter>, <index>)
```

## Exemples SQL

```sql
SELECT SPLIT_PART('a-b-c', '-', 2);

┌───┐
│ b  │
└───┘
```
