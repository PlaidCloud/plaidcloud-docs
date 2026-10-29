---
title: NULLIF (Lakehouse v1)
description: NULLIF — renvoie NULL si deux expressions sont égales.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/nullif.md
---

Renvoie NULL si deux expressions sont égales ; sinon, renvoie expr1. Les deux expressions doivent avoir le même type de données.

## Syntaxe Analyze

```python
func.nullif(<expr1>, <expr2>)
```

## Exemples Analyze

```python
func.nullif(0, null) 

┌──────────────────────┐
│ func.nullif(0, null) │
├──────────────────────┤
│                    0 │
└──────────────────────┘
```

## Syntaxe SQL

```sql
NULLIF(<expr1>, <expr2>)
```

## Exemples SQL

```sql
SELECT NULLIF(0, NULL);

┌─────────────────┐
│ nullif(0, null) │
├─────────────────┤
│               0 │
└─────────────────┘
```
