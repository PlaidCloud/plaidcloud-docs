---
title: ATAN2 (Lakehouse v2)
description: ATAN2 — 返回 y/x 的反正切值，并根据符号确定象限。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/atan2.md
---

返回 y/x 的反正切值，并根据符号确定象限。

## Analyze 语法

```python
func.atan2(<y>, <x>)
```

## Analyze 示例

```python
func.atan2(1, 1)

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```

## SQL 语法

```sql
ATAN2(<y>, <x>)
```

## SQL 示例

```sql
SELECT ATAN2(1, 1);

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```
