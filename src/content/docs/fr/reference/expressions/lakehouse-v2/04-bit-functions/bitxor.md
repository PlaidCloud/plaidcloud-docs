---
title: BITXOR (Lakehouse v2)
description: BITXOR — renvoie le OU exclusif (XOR) bit à bit de deux valeurs numériques.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitxor.md
---

Renvoie le OU exclusif (XOR) bit à bit de deux valeurs numériques.

## Syntaxe Analyze

```python
func.bitxor(<x>, <y>)
```

## Exemples Analyze

```python
func.bitxor(12, 10)

┌───┐
│ 6  │
└───┘
```

## Syntaxe SQL

```sql
BITXOR(<x>, <y>)
```

## Exemples SQL

```sql
SELECT BITXOR(12, 10);

┌───┐
│ 6  │
└───┘
```
