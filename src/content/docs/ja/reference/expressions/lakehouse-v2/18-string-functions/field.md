---
title: FIELD（Lakehouse v2）
description: FIELD — 引数のリスト内で値が見つかった位置（インデックス）を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/field.md
---

引数のリスト内で値が見つかった位置（インデックス）を返します。

## Analyze 構文

```python
func.field(<str>, <val1>, <val2>[, ...])
```

## Analyze の例

```python
func.field('b', 'a', 'b', 'c')

┌───┐
│ 2  │
└───┘
```

## SQL 構文

```sql
FIELD(<str>, <val1>, <val2>[, ...])
```

## SQL の例

```sql
SELECT FIELD('b', 'a', 'b', 'c');

┌───┐
│ 2  │
└───┘
```
