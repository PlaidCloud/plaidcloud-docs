---
title: BITAND (Lakehouse v2)
description: BITAND — renvoie le ET bit à bit de deux valeurs numériques.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitand.md
---

Renvoie le ET bit à bit de deux valeurs numériques.

## Syntaxe Analyze

```python
func.bitand(<x>, <y>)
```

## Exemples Analyze

```python
func.bitand(12, 10)

┌───┐
│ 8  │
└───┘
```

## Syntaxe SQL

```sql
BITAND(<x>, <y>)
```

## Exemples SQL

```sql
SELECT BITAND(12, 10);

┌───┐
│ 8  │
└───┘
```
