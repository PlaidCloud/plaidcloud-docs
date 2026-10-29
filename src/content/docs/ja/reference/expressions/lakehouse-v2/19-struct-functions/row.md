---
title: ROW（Lakehouse v2）
description: ROW — 値のリストから構造体を作成します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/19-struct-functions/row.md
---

値のリストから構造体を作成します。

## Analyze 構文

```python
func.row(<val1>[, <val2>, ...])
```

## Analyze の例

```python
func.row('Alice', 30)

┌────────────────────────────┐
│ {'col1':'Alice','col2':30}  │
└────────────────────────────┘
```

## SQL 構文

```sql
ROW(<val1>[, <val2>, ...])
```

## SQL の例

```sql
SELECT ROW('Alice', 30);

┌────────────────────────────┐
│ {"col1":"Alice","col2":30}  │
└────────────────────────────┘
```
