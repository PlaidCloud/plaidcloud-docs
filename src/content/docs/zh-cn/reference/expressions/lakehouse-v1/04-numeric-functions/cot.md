---
title: COT（Lakehouse v1）
description: COT——返回 x 的余切，其中 x 以弧度表示。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/cot.md
---

返回 `x` 的余切，其中 `x` 以弧度表示。

## Analyze 语法

```python
func.cot( <x> )
```

## Analyze 示例

```python
func.cot(12) 

┌─────────────────────┐
│    func.cot(12)     │
├─────────────────────┤
│ -1.5726734063976895 │
└─────────────────────┘
```

## SQL 语法

```sql
COT( <x> )
```

## SQL 示例

```sql
SELECT COT(12);

┌─────────────────────┐
│       cot(12)       │
├─────────────────────┤
│ -1.5726734063976895 │
└─────────────────────┘
```
