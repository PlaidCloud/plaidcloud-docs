---
title: RTRIM (Lakehouse v2)
description: RTRIM — supprime les espaces de fin ou les caractères spécifiés à la fin d'une chaîne.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/rtrim.md
---

Supprime les espaces de fin ou les caractères spécifiés à la fin d'une chaîne.

## Syntaxe Analyze

```python
func.rtrim(<str>)
```

## Exemples Analyze

```python
func.rtrim('hello   ')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## Syntaxe SQL

```sql
RTRIM(<str>)
```

## Exemples SQL

```sql
SELECT RTRIM('hello   ');

┌───────┐
│ hello  │
└───────┘
```
