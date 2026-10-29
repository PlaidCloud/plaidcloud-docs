---
title: CHAR (Lakehouse v2)
description: CHAR — renvoie le caractère correspondant à un code ASCII donné.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/char.md
---

Renvoie le caractère correspondant à un code ASCII donné.

## Syntaxe Analyze

```python
func.char(<code>)
```

## Exemples Analyze

```python
func.char(65)

┌─────┐
│ 'A'  │
└─────┘
```

## Syntaxe SQL

```sql
CHAR(<code>)
```

## Exemples SQL

```sql
SELECT CHAR(65);

┌───┐
│ A  │
└───┘
```
