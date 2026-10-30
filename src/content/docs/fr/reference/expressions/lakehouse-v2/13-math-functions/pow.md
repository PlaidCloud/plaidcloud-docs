---
title: POW (Lakehouse v2)
description: POW — renvoie un nombre élevé à la puissance d'un autre nombre.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/pow.md
---

Renvoie un nombre élevé à la puissance d'un autre nombre.

## Syntaxe Analyze

```python
func.pow(<x>, <y>)
```

## Exemples Analyze

```python
func.pow(2, 10)

┌────────┐
│ 1024.0  │
└────────┘
```

## Syntaxe SQL

```sql
POW(<x>, <y>)
```

## Exemples SQL

```sql
SELECT POW(2, 10);

┌────────┐
│ 1024.0  │
└────────┘
```
