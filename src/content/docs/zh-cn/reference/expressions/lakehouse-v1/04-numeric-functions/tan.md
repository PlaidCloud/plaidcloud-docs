---
title: TAN（Lakehouse v1）
description: TAN——返回 x 的正切，其中 x 以弧度表示。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/tan.md
---

返回 `x` 的正切，其中 `x` 以弧度表示。

## Analyze 语法

```python
func.tan( <x> )
```

## Analyze 示例

```python
func.tan(90)

┌────────────────────┐
│    func.tan(90)    │
├────────────────────┤
│ -1.995200412208242 │
└────────────────────┘
```

## SQL 语法

```sql
TAN( <x> )
```

## SQL 示例

```sql
SELECT TAN(90);

┌────────────────────┐
│       tan(90)      │
├────────────────────┤
│ -1.995200412208242 │
└────────────────────┘
```
