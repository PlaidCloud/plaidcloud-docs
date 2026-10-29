---
title: SAFE_DIVIDE（Lakehouse v1）
description: SAFE_DIVIDE — 2 つの数を割り算し、分母が 0 の場合にエラーにならず、指定した値を返す PlaidCloud の関数です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/safe-divide.md
---

すべての Lakehouse エンジンで使用できる PlaidCloud の関数です。最初の数を 2 番目の数で割ります。分母が 0 の場合、またはいずれかの側が NULL の場合、結果は 3 番目の値になります。NULL を返したい場合は `None` を渡します。Lakehouse v1 では 3 つの引数がすべて必須です。両側は最初に `DECIMAL(38, 10)` にキャストされるため、整数列でも切り捨てなしで割り算できます。

## Analyze 構文

```python
func.safe_divide(<numerator>, <denominator>, <divide_by_zero_value>)
```

## Analyze の例

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

## 同等の SQL

この名前の SQL 関数はありません。式は次のようにコンパイルされます。

```sql
COALESCE(CAST(<numerator> AS DECIMAL(38, 10)) / NULLIF(CAST(<denominator> AS DECIMAL(38, 10)), 0), <divide_by_zero_value>)
```
