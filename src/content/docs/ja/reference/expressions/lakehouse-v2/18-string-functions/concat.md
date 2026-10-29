---
title: CONCAT（Lakehouse v2）
description: CONCAT — 2つ以上の文字列を連結します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/concat.md
---

2つ以上の文字列を連結します。

## Analyze 構文

```python
func.concat(<str1>, <str2>[, ...])
```

## Analyze の例

```python
func.concat('Star', 'Rocks')

┌─────────────┐
│ 'StarRocks'  │
└─────────────┘
```

## SQL 構文

```sql
CONCAT(<str1>, <str2>[, ...])
```

## SQL の例

```sql
SELECT CONCAT('Star', 'Rocks');

┌───────────┐
│ StarRocks  │
└───────────┘
```
