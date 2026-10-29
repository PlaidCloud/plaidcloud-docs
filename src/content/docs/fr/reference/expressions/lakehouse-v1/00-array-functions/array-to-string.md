---
title: ARRAY_TO_STRING (Lakehouse v1)
description: "ARRAY_TO_STRING : concatène les éléments d'un tableau en une seule chaîne, à l'aide d'un séparateur donné."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-to-string.md
---

Concatène les éléments d'un tableau en une seule chaîne, à l'aide d'un séparateur donné.

## Syntaxe Analyze

```python
func.array_to_string( <array>, '<separator>' )
```

## Exemples Analyze

```python
func.array_to_string(['apple', 'banana', 'cherry'], ', ') 

┌────────────────────────────────────────────────────────────┐
│ func.array_to_string(['apple', 'banana', 'cherry'], ', ')  │
├────────────────────────────────────────────────────────────┤
│ Apple, Banana, Cherry                                      │
└────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
ARRAY_TO_STRING( <array>, '<separator>' )
```

## Exemples SQL

```sql
SELECT ARRAY_TO_STRING(['Apple', 'Banana', 'Cherry'], ', ');

┌──────────────────────────────────────────────────────┐
│ array_to_string(['apple', 'banana', 'cherry'], ', ') │
├──────────────────────────────────────────────────────┤
│ Apple, Banana, Cherry                                │
└──────────────────────────────────────────────────────┘
```
