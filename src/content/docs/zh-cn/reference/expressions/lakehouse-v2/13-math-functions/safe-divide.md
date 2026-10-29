---
title: SAFE_DIVIDE (Lakehouse v2)
description: SAFE_DIVIDE — PlaidCloud 函数，用于两数相除，并在分母为零时返回指定的值，而不是报错。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/safe-divide.md
---

PlaidCloud 函数，所有 Lakehouse 引擎均可使用。将第一个数除以第二个数。分母为零或任一侧为 NULL 时，结果为 NULL；如果提供了第三个值，则返回该值。运算前会先将两侧转换为 `DECIMAL(38, 10)`，因此整数列相除不会被截断。

## Analyze 语法

```python
func.safe_divide(<numerator>, <denominator>, <divide_by_zero_value>)

func.safe_divide(<numerator>, <denominator>)
```

## Analyze 示例

```python
func.safe_divide(table.revenue, table.units, 0)

| revenue | units | safe_divide |
|---------|-------|-------------|
| 100     | 8     | 12.5        |
| 100     | 0     | 0           |
| 100     | NULL  | 0           |
```

```python
func.safe_divide(table.revenue, table.units, None)

| revenue | units | safe_divide |
|---------|-------|-------------|
| 100     | 8     | 12.5        |
| 100     | 0     | NULL        |
```

## SQL 等效写法

没有同名的 SQL 函数。该表达式会编译为：

```sql
COALESCE(CAST(<numerator> AS DECIMAL(38, 10)) / NULLIF(CAST(<denominator> AS DECIMAL(38, 10)), 0), <divide_by_zero_value>)
```

如果没有第三个参数，则不使用 COALESCE，分母为零时结果为 NULL：

```sql
CAST(<numerator> AS DECIMAL(38, 10)) / NULLIF(CAST(<denominator> AS DECIMAL(38, 10)), 0)
```
