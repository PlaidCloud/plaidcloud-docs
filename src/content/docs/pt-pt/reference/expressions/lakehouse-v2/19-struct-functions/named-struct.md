---
title: NAMED_STRUCT (Lakehouse v2)
description: NAMED_STRUCT — cria um struct com nomes de campo e valores especificados.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/19-struct-functions/named-struct.md
---

Cria um struct com nomes de campo e valores especificados.

## Sintaxe do Analyze

```python
func.named_struct(<name1>, <val1>[, <name2>, <val2>, ...])
```

## Exemplos do Analyze

```python
func.named_struct('name', 'Alice', 'age', 30)

┌───────────────────────────┐
│ {'name':'Alice','age':30}  │
└───────────────────────────┘
```

## Sintaxe SQL

```sql
NAMED_STRUCT(<name1>, <val1>[, <name2>, <val2>, ...])
```

## Exemplos SQL

```sql
SELECT NAMED_STRUCT('name', 'Alice', 'age', 30);

┌───────────────────────────┐
│ {"name":"Alice","age":30}  │
└───────────────────────────┘
```
