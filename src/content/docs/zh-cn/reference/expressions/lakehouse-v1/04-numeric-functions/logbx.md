---
title: "LOG(b, x)（Lakehouse v1）"
description: LOG(b, x)——返回 x 以 b 为底的对数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/logbx.md
---

返回 `x` 以 b 为底的对数。如果 `x` 小于或等于 0.0E0，则函数返回 NULL。

## Analyze 语法

```python
func.log( <b, x> )
```

## Analyze 示例

```python
func.log(2, 65536)

┌────────────────────┐
│ func.log(2, 65536) │
├────────────────────┤
│                 16 │
└────────────────────┘
```

## SQL 语法

```sql
LOG( <b, x> )
```

## SQL 示例

```sql
SELECT LOG(2, 65536);

┌───────────────┐
│ log(2, 65536) │
├───────────────┤
│            16 │
└───────────────┘
```
