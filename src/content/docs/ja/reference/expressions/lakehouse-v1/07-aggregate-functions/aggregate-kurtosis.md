---
title: KURTOSIS (Lakehouse v1)
description: KURTOSIS — すべての入力値の超過尖度（正規分布と比較した尖り具合）を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-kurtosis.md
---

集計関数です。

`KURTOSIS()` 関数は、すべての入力値の超過尖度を返します。

## Analyzeの構文

```python
func.kurtosis(<expr>)
```

## Analyzeの例

```python
func.kurtosis(table.price).alias('excess_kurtosis')

|     excess_kurtosis     |
|-------------------------|
| 0.06818181325581445     |
```

## SQLの構文

```sql
KURTOSIS(<expr>)
```

## 引数

| 引数 | 説明                     |
|-----------| -----------                     |
| `<expr>`  | 任意の数値式        |

## 戻り値の型

Nullable Float64。

## SQLの例

**テーブルの作成とサンプルデータの挿入**
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

**クエリのデモ: Apple の株価の超過尖度を計算する**

```sql
SELECT KURTOSIS(price) AS excess_kurtosis
FROM stock_prices
WHERE stock_symbol = 'AAPL';
```

**結果**

```sql
|     excess_kurtosis     |
|-------------------------|
| 0.06818181325581445     |
```
