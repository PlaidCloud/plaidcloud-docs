---
title: ACOS（Lakehouse v1）
description: ACOS——返回 x 的反余弦，即余弦值为 x 的角度值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/acos.md
---

返回 `x` 的反余弦，即余弦值为 `x` 的角度值。如果 `x` 不在 -1 到 1 的范围内，则返回 NULL。

## Analyze 语法

```python
func.abs( <x> )
```

## Analyze 示例

```python
func.abs(1)

┌──────────────┐
│ func.acos(1) │
├──────────────┤
│            0 │
└──────────────┘
```

## SQL 语法

```sql
ACOS( <x> )
```

## SQL 示例

```sql
SELECT ACOS(1);

┌─────────┐
│ acos(1) │
├─────────┤
│       0 │
└─────────┘
```
