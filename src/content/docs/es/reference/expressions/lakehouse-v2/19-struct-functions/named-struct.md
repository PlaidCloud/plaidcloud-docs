---
title: NAMED_STRUCT (Lakehouse v2)
description: NAMED_STRUCT — Crea una estructura con los nombres de campo y los valores especificados.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/19-struct-functions/named-struct.md
---

Crea una estructura con los nombres de campo y los valores especificados.

## Sintaxis de Analyze

```python
func.named_struct(<name1>, <val1>[, <name2>, <val2>, ...])
```

## Ejemplos de Analyze

```python
func.named_struct('name', 'Alice', 'age', 30)

┌───────────────────────────┐
│ {'name':'Alice','age':30}  │
└───────────────────────────┘
```

## Sintaxis de SQL

```sql
NAMED_STRUCT(<name1>, <val1>[, <name2>, <val2>, ...])
```

## Ejemplos de SQL

```sql
SELECT NAMED_STRUCT('name', 'Alice', 'age', 30);

┌───────────────────────────┐
│ {"name":"Alice","age":30}  │
└───────────────────────────┘
```
