---
title: NAMED_STRUCT (Lakehouse v2)
description: NAMED_STRUCT — tworzy strukturę o podanych nazwach pól i wartościach.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/19-struct-functions/named-struct.md
---

Tworzy strukturę o podanych nazwach pól i wartościach.

## Składnia Analyze

```python
func.named_struct(<name1>, <val1>[, <name2>, <val2>, ...])
```

## Przykłady Analyze

```python
func.named_struct('name', 'Alice', 'age', 30)

┌───────────────────────────┐
│ {'name':'Alice','age':30}  │
└───────────────────────────┘
```

## Składnia SQL

```sql
NAMED_STRUCT(<name1>, <val1>[, <name2>, <val2>, ...])
```

## Przykłady SQL

```sql
SELECT NAMED_STRUCT('name', 'Alice', 'age', 30);

┌───────────────────────────┐
│ {"name":"Alice","age":30}  │
└───────────────────────────┘
```
