---
title: RADIANS（Lakehouse v1）
description: RADIANS——将参数 x 从度数转换为弧度并返回。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/radians.md
---

将参数 `x` 从度数转换为弧度并返回。

## Analyze 语法

```python
func.radians( <x> )
```

## Analyze 示例

```python
func.radians(90)

┌────────────────────┐
│  func.radians(90)  │
├────────────────────┤
│ 1.5707963267948966 │
└────────────────────┘
```

## SQL 语法

```sql
RADIANS( <x> )
```

## SQL 示例

```sql
SELECT RADIANS(90);

┌────────────────────┐
│     radians(90)    │
├────────────────────┤
│ 1.5707963267948966 │
└────────────────────┘
```
