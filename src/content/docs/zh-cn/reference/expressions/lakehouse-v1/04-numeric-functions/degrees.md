---
title: DEGREES (Lakehouse v1)
description: DEGREES — 将参数 x 从弧度转换为度并返回，其中 x 以弧度表示。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/degrees.md
---

返回参数 `x` 从弧度转换为度后的值，其中 `x` 以弧度表示。

## Analyze 语法

```python
func.degrees( <x> )
```

## Analyze 示例

```python
func.degrees(func.pi())

┌─────────────────────────┐
│ func.degrees(func.pi()) │
├─────────────────────────┤
│                     180 │
└─────────────────────────┘
```

## SQL 语法

```sql
DEGREES( <x> )
```

## SQL 示例

```sql
SELECT DEGREES(PI());

┌───────────────┐
│ degrees(pi()) │
├───────────────┤
│           180 │
└───────────────┘
```
