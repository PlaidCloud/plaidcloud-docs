---
title: INITCAP (Lakehouse v2)
description: INITCAP — met en majuscule la première lettre de chaque mot d'une chaîne.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/initcap.md
---

Met en majuscule la première lettre de chaque mot d'une chaîne.

## Syntaxe Analyze

```python
func.initcap(<str>)
```

## Exemples Analyze

```python
func.initcap('hello world')

┌───────────────┐
│ 'Hello World'  │
└───────────────┘
```

## Syntaxe SQL

```sql
INITCAP(<str>)
```

## Exemples SQL

```sql
SELECT INITCAP('hello world');

┌─────────────┐
│ Hello World  │
└─────────────┘
```
