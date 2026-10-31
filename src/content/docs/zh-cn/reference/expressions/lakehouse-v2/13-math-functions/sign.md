---
title: SIGN (Lakehouse v2)
description: "SIGN — 返回数值的符号：-1、0 或 1。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sign.md
---

返回数值的符号：-1、0 或 1。

## Analyze 语法

```python
func.sign(<x>)
```

## Analyze 示例

```python
func.sign(-42)

┌────┐
│ -1  │
└────┘
```

## SQL 语法

```sql
SIGN(<x>)
```

## SQL 示例

```sql
SELECT SIGN(-42);

┌────┐
│ -1  │
└────┘
```
