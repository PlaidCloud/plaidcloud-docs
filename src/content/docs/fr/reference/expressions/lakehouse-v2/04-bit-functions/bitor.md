---
title: BITOR (Lakehouse v2)
description: BITOR — renvoie le OU bit à bit de deux valeurs numériques.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitor.md
---

Renvoie le OU bit à bit de deux valeurs numériques.

## Syntaxe Analyze

```python
func.bitor(<x>, <y>)
```

## Exemples Analyze

```python
func.bitor(12, 10)

┌────┐
│ 14  │
└────┘
```

## Syntaxe SQL

```sql
BITOR(<x>, <y>)
```

## Exemples SQL

```sql
SELECT BITOR(12, 10);

┌────┐
│ 14  │
└────┘
```
