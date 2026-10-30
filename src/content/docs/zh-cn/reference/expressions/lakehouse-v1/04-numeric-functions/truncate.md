---
title: TRUNCATE（Lakehouse v1）
description: TRUNCATE——返回截断到 d 位小数的数字 x。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/truncate.md
---

返回截断到 `d` 位小数的数字 `x`。如果 `d` 为 0，则结果没有小数点或小数部分。`d` 可以为负数，使值 `x` 小数点左侧的 `d` 位数字变为零。`d` 的最大绝对值为 30；超过 30（或 -30）的数位会被截断。

## Analyze 语法

```python
func.truncate( <x, d> )
```

## Analyze 示例

```python
func.truncate(1.223, 1)

┌─────────────────────────┐
│ func.truncate(1.223, 1) │
├─────────────────────────┤
│                     1.2 │
└─────────────────────────┘
```

## SQL 语法

```sql
TRUNCATE( <x, d> )
```

## SQL 示例

```sql
SELECT TRUNCATE(1.223, 1);

┌────────────────────┐
│ truncate(1.223, 1) │
├────────────────────┤
│ 1.2                │
└────────────────────┘
```
