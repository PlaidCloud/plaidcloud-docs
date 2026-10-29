---
title: KURTOSIS (Lakehouse v1)
description: KURTOSIS：返回所有输入值的超额峰度（相对于正态分布的尖峰程度）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-kurtosis.md
---

聚合函数。

`KURTOSIS()` 函数返回所有输入值的超额峰度。

## Analyze 语法

```python
func.kurtosis(<expr>)
```

## Analyze 示例

```python
func.kurtosis(table.price).alias('excess_kurtosis')

|     excess_kurtosis     |
|-------------------------|
| 0.06818181325581445     |
```

## SQL 语法

```sql
KURTOSIS(<expr>)
```

## 参数

| 参数 | 说明                     |
|-----------| -----------                     |
| `<expr>`  | 任意数值表达式        |

## 返回类型

可为空的 Float64。

## SQL 示例

**创建表并插入示例数据**
```sql
CREATE TABLE stock_prices (
  id INT,
  stock_symbol VARCHAR,
  price FLOAT
);

INSERT INTO stock_prices (id, stock_symbol, price)
VALUES (1, 'AAPL', 150),
       (2, 'AAPL', 152),
       (3, 'AAPL', 148),
       (4, 'AAPL', 160),
       (5, 'AAPL', 155);
```

**查询演示：计算 Apple 股票价格的超额峰度**

```sql
SELECT KURTOSIS(price) AS excess_kurtosis
FROM stock_prices
WHERE stock_symbol = 'AAPL';
```

**结果**

```sql
|     excess_kurtosis     |
|-------------------------|
| 0.06818181325581445     |
```
