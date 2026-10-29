---
title: NAMED_STRUCT（Lakehouse v2）
description: NAMED_STRUCT — 指定したフィールド名と値で構造体を作成します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/19-struct-functions/named-struct.md
---

指定したフィールド名と値で構造体を作成します。

## Analyze 構文

```python
func.named_struct(<name1>, <val1>[, <name2>, <val2>, ...])
```

## Analyze の例

```python
func.named_struct('name', 'Alice', 'age', 30)

┌───────────────────────────┐
│ {'name':'Alice','age':30}  │
└───────────────────────────┘
```

## SQL 構文

```sql
NAMED_STRUCT(<name1>, <val1>[, <name2>, <val2>, ...])
```

## SQL の例

```sql
SELECT NAMED_STRUCT('name', 'Alice', 'age', 30);

┌───────────────────────────┐
│ {"name":"Alice","age":30}  │
└───────────────────────────┘
```
