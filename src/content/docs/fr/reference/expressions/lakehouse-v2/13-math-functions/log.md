---
title: LOG (Lakehouse v2)
description: LOG — renvoie le logarithme d'un nombre dans une base spécifiée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/log.md
---

Renvoie le logarithme d'un nombre dans une base spécifiée.

## Syntaxe Analyze

```python
func.log(<base>, <x>)
```

## Exemples Analyze

```python
func.log(10, 100)

┌─────┐
│ 2.0  │
└─────┘
```

## Syntaxe SQL

```sql
LOG(<base>, <x>)
```

## Exemples SQL

```sql
SELECT LOG(10, 100);

┌─────┐
│ 2.0  │
└─────┘
```
