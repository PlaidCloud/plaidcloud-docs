---
title: TYPEOF (Lakehouse v1)
description: TYPEOF：TYPEOF 函数用于返回数据类型的名称。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/typeof.md
---

TYPEOF 函数用于返回数据类型的名称。

## Analyze 语法

```python
func.typeof( <expr> )
```

## Analyze 示例

```python
func.typeof(1)
┌──────────────────┐
│ func.typeof(1)   │
├──────────────────┤
│ INT              │
└──────────────────┘
```

## SQL 语法

```sql
TYPEOF( <expr> )
```

## 参数

| 参数 | 说明 |
| ----------- | ----------- |
| `<expr>` | 任意表达式。 <br /> 可以是列名、其他函数的结果或数学运算。

## 返回类型

字符串

## SQL 示例

```sql
SELECT typeof(1::INT);
┌──────────────────┐
│ typeof(1::Int32) │
├──────────────────┤
│ INT              │
└──────────────────┘
```
