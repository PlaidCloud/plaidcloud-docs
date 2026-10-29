---
title: ASIN（Lakehouse v1）
description: ASIN——返回 x 的反正弦，即正弦值为 x 的角度值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/asin.md
---

返回 `x` 的反正弦，即正弦值为 `x` 的角度值。如果 `x` 不在 -1 到 1 的范围内，则返回 NULL。

## Analyze 语法

```python
func.asin( <x> )
```

## Analyze 示例

```python
func.asin(0.2)

┌────────────────────┐
│   func.asin(0.2)   │
├────────────────────┤
│ 0.2013579207903308 │
└────────────────────┘
```

## SQL 语法

```sql
ASIN( <x> )
```

## SQL 示例

```sql
SELECT ASIN(0.2);

┌────────────────────┐
│      asin(0.2)     │
├────────────────────┤
│ 0.2013579207903308 │
└────────────────────┘
```
