---
title: NAMED_STRUCT (Lakehouse v2)
description: NAMED_STRUCT — crée une structure avec des noms et des valeurs de champs spécifiés.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/19-struct-functions/named-struct.md
---

Crée une structure avec des noms et des valeurs de champs spécifiés.

## Syntaxe Analyze

```python
func.named_struct(<name1>, <val1>[, <name2>, <val2>, ...])
```

## Exemples Analyze

```python
func.named_struct('name', 'Alice', 'age', 30)

┌───────────────────────────┐
│ {'name':'Alice','age':30}  │
└───────────────────────────┘
```

## Syntaxe SQL

```sql
NAMED_STRUCT(<name1>, <val1>[, <name2>, <val2>, ...])
```

## Exemples SQL

```sql
SELECT NAMED_STRUCT('name', 'Alice', 'age', 30);

┌───────────────────────────┐
│ {"name":"Alice","age":30}  │
└───────────────────────────┘
```
