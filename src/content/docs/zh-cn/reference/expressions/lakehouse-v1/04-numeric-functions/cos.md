---
title: COS（Lakehouse v1）
description: COS——返回 x 的余弦，其中 x 以弧度表示。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/cos.md
---

返回 `x` 的余弦，其中 `x` 以弧度表示。

## Analyze 语法

```python
func.cos( <x> )
```

## Analyze 示例

```python
func.cos(func.pi())

┌─────────────────────┐
│ func.cos(func.pi()) │
├─────────────────────┤
│                  -1 │
└─────────────────────┘
```

## SQL 语法

```sql
COS( <x> )
```

## SQL 示例

```sql
SELECT COS(PI());

┌───────────┐
│ cos(pi()) │
├───────────┤
│        -1 │
└───────────┘
```
