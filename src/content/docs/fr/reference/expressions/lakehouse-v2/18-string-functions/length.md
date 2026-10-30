---
title: LENGTH (Lakehouse v2)
description: LENGTH — renvoie la longueur d'une chaîne en octets.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/length.md
---

Renvoie la longueur d'une chaîne en octets.

## Syntaxe Analyze

```python
func.length(<str>)
```

## Exemples Analyze

```python
func.length('hello')

┌───┐
│ 5  │
└───┘
```

## Syntaxe SQL

```sql
LENGTH(<str>)
```

## Exemples SQL

```sql
SELECT LENGTH('hello');

┌───┐
│ 5  │
└───┘
```
