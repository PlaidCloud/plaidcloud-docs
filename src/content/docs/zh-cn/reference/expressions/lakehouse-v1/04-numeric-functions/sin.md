---
title: SIN（Lakehouse v1）
description: SIN——返回 x 的正弦，其中 x 以弧度表示。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/sin.md
---

返回 `x` 的正弦，其中 `x` 以弧度表示。

## Analyze 语法

```python
func.sin( <x> )
```

## Analyze 示例

```python
func.sin(90)

┌────────────────────┐
│    func.sin(90)    │
├────────────────────┤
│ 0.8939966636005579 │
└────────────────────┘
```

## SQL 语法

```sql
SIN( <x> )
```

## SQL 示例

```sql
SELECT SIN(90);

┌────────────────────┐
│       sin(90)      │
├────────────────────┤
│ 0.8939966636005579 │
└────────────────────┘
```
