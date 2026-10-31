---
title: NAMED_STRUCT (Lakehouse v2)
description: NAMED_STRUCT — Erstellt ein Struct mit angegebenen Feldnamen und Werten.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/19-struct-functions/named-struct.md
---

Erstellt ein Struct mit angegebenen Feldnamen und Werten.

## Analyze-Syntax

```python
func.named_struct(<name1>, <val1>[, <name2>, <val2>, ...])
```

## Analyze-Beispiele

```python
func.named_struct('name', 'Alice', 'age', 30)

┌───────────────────────────┐
│ {'name':'Alice','age':30}  │
└───────────────────────────┘
```

## SQL-Syntax

```sql
NAMED_STRUCT(<name1>, <val1>[, <name2>, <val2>, ...])
```

## SQL-Beispiele

```sql
SELECT NAMED_STRUCT('name', 'Alice', 'age', 30);

┌───────────────────────────┐
│ {"name":"Alice","age":30}  │
└───────────────────────────┘
```
