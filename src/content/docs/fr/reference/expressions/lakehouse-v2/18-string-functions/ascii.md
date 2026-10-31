---
title: ASCII (Lakehouse v2)
description: ASCII — renvoie le code ASCII du premier caractère d'une chaîne.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ascii.md
---

Renvoie le code ASCII du premier caractère d'une chaîne.

## Syntaxe Analyze

```python
func.ascii(<str>)
```

## Exemples Analyze

```python
func.ascii('A')

┌────┐
│ 65  │
└────┘
```

## Syntaxe SQL

```sql
ASCII(<str>)
```

## Exemples SQL

```sql
SELECT ASCII('A');

┌────┐
│ 65  │
└────┘
```
