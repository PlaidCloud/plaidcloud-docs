---
title: RAND(n)（Lakehouse v1）
description: RAND(n)——返回范围 0 &lt;= v &lt; 1.0 内的随机浮点值 v。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/randn.md
---

返回范围 0 &lt;= v &lt; 1.0 内的随机浮点值 v。要获得范围 i &lt;= R &lt; j 内的随机整数 R，请使用表达式 FLOOR(i + RAND() * (j − i))。参数 `n` 用作种子值。对于相同的参数值，RAND(n) 每次返回相同的值，因此会生成可重复的列值序列。

## Analyze 语法

```python
func.rand( <n>)
```

## Analyze 示例

```python
func.rand(1)

┌────────────────────┐
│    func.rand(1)    │
├────────────────────┤
│ 0.7133693869548766 │
└────────────────────┘
```

## SQL 语法

```sql
RAND( <n>)
```

## SQL 示例

```sql
SELECT RAND(1);

┌────────────────────┐
│       rand(1)      │
├────────────────────┤
│ 0.7133693869548766 │
└────────────────────┘
```
