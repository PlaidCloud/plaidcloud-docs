---
title: IS_NULL（Lakehouse v1）
description: IS_NULL — 値が NULL かどうかを確認します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/is-null.md
---

値が NULL かどうかを確認します。

## Analyze 構文

```python
func.is_null(<expr>)
```

## Analyze の例

```python
func.is_null(1)

┌─────────────────┐
│ func.is_null(1) │
├─────────────────┤
│ false           │
└─────────────────┘
```

## SQL 構文

```sql
IS_NULL(<expr>)
```

## SQL の例

```sql
SELECT IS_NULL(1);

┌────────────┐
│ is_null(1) │
├────────────┤
│ false      │
└────────────┘
```
