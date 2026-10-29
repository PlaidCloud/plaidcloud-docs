---
title: RAND()（Lakehouse v1）
description: RAND()——返回范围 0 <= v < 1 内的随机浮点值 v。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/rand.md
---

返回范围 0 &lt;= v &lt; 1.0 内的随机浮点值 v。要获得范围 i &lt;= R &lt; j 内的随机整数 R，请使用表达式 FLOOR(i + RAND() * (j − i))。

## Analyze 语法

```python
func.rand()
```

## Analyze 示例

```python
func.rand()

┌────────────────────┐
│    func.rand()     │
├────────────────────┤
│ 0.5191511074382174 │
└────────────────────┘
```

## SQL 语法

```sql
RAND()
```

## SQL 示例

```sql
SELECT RAND();

┌────────────────────┐
│       rand()       │
├────────────────────┤
│ 0.5191511074382174 │
└────────────────────┘
```
