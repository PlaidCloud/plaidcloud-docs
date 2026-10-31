---
title: IS_NOT_NULL（Lakehouse v1）
description: IS_NOT_NULL — 値が NULL でないかどうかを確認します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/is-not-null.md
---

値が NULL でないかどうかを確認します。

## Analyze 構文

```python
func.is_not_null(<expr>)
```

## Analyze の例

```python
func.is_not_null(1)

┌─────────────────────┐
│ func.is_not_null(1) │
├─────────────────────┤
│ true                │
└─────────────────────┘
```

## SQL 構文

```sql
IS_NOT_NULL(<expr>)
```

## SQL の例

```sql
SELECT IS_NOT_NULL(1);

┌────────────────┐
│ is_not_null(1) │
├────────────────┤
│ true           │
└────────────────┘
```
