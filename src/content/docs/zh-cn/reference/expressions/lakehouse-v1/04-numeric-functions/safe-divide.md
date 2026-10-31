---
title: SAFE_DIVIDE（Lakehouse v1）
description: SAFE_DIVIDE——PlaidCloud 函数，用于两数相除，并在分母为零时返回您指定的值而不是失败。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/safe-divide.md
---

PlaidCloud 函数，在所有 Lakehouse 引擎上均可使用。将第一个数除以第二个数。当分母为零或任一侧为 NULL 时，结果为第三个值；传入 `None` 可得到 NULL。在 Lakehouse v1 上，三个参数均为必填。两侧会先转换为 `DECIMAL(38, 10)`，因此整数列相除时不会被截断。

## Analyze 语法

```python
func.safe_divide(<numerator>, <denominator>, <divide_by_zero_value>)
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

## 等效 SQL

没有同名的 SQL 函数。该表达式会编译为：

```sql
COALESCE(CAST(<numerator> AS DECIMAL(38, 10)) / NULLIF(CAST(<denominator> AS DECIMAL(38, 10)), 0), <divide_by_zero_value>)
```
