---
title: SAFE_DIVIDE (Lakehouse v2)
description: SAFE_DIVIDE — 2つの数値を割り、分母がゼロの場合にエラーにならず、指定した値を返すPlaidCloudの関数です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/safe-divide.md
---

すべてのレイクハウスエンジンで利用できるPlaidCloudの関数です。1番目の数値を2番目の数値で割ります。分母がゼロの場合、またはどちらかの側がNULLの場合、結果はNULLになります。3番目の値を指定した場合は、代わりにその値が返されます。最初に両辺を `DECIMAL(38, 10)` にキャストするため、整数列でも切り捨てなしで除算できます。

## Analyzeの構文

```python
func.safe_divide(<numerator>, <denominator>, <divide_by_zero_value>)

func.safe_divide(<numerator>, <denominator>)
```

## Analyzeの例

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

## SQLでの相当式

この名前のSQL関数はありません。式は次のようにコンパイルされます。

```sql
COALESCE(CAST(<numerator> AS DECIMAL(38, 10)) / NULLIF(CAST(<denominator> AS DECIMAL(38, 10)), 0), <divide_by_zero_value>)
```

3番目の引数を指定しない場合は COALESCE が付かず、分母がゼロのときの結果はNULLになります。

```sql
CAST(<numerator> AS DECIMAL(38, 10)) / NULLIF(CAST(<denominator> AS DECIMAL(38, 10)), 0)
```
