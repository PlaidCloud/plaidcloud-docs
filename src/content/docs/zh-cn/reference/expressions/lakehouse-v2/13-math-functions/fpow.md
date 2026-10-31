---
title: FPOW (Lakehouse v2)
description: FPOW — `POW` 的别名。参见 [POW](../pow/)。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/fpow.md
---

`POW` 的别名。参见 [POW](../pow/)。

## Analyze 语法

```python
func.fpow(2, 10)
```

## Analyze 示例

```python
func.fpow(2, 10)

┌────────┐
│ 1024.0 │
└────────┘
```

## SQL 语法

```sql
FPOW(<x>)
```

## SQL 示例

```sql
SELECT FPOW(2, 10);

┌────────┐
│ 1024.0 │
└────────┘
```
