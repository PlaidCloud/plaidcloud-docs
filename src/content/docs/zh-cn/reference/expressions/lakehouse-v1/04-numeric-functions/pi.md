---
title: PI（Lakehouse v1）
description: PI——以浮点值形式返回 π 的值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/pi.md
---

以浮点值形式返回 π 的值。

## Analyze 语法

```python
func.pi()
```

## Analyze 示例

```python
func.pi()

┌───────────────────┐
│     func.pi()     │
├───────────────────┤
│ 3.141592653589793 │
└───────────────────┘
```

## SQL 语法

```sql
PI()
```

## SQL 示例

```sql
SELECT PI();

┌───────────────────┐
│        pi()       │
├───────────────────┤
│ 3.141592653589793 │
└───────────────────┘
```
