---
title: ATAN（Lakehouse v1）
description: ATAN——返回 x 的反正切，即正切值为 x 的角度值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/atan.md
---

返回 `x` 的反正切，即正切值为 `x` 的角度值。

## Analyze 语法

```python
func.atan( <x> )
```

## Analyze 示例

```python
func.atan(-2)

┌─────────────────────┐
│  func.atan((- 2))   │
├─────────────────────┤
│ -1.1071487177940906 │
└─────────────────────┘
```

## SQL 语法

```sql
ATAN( <x> )
```

## SQL 示例

```sql
SELECT ATAN(-2);

┌─────────────────────┐
│     atan((- 2))     │
├─────────────────────┤
│ -1.1071487177940906 │
└─────────────────────┘
```
