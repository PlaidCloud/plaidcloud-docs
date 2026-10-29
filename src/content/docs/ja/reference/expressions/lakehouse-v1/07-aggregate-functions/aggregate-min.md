---
title: MIN (Lakehouse v1)
description: MIN — 値の集合から最小値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-min.md
---

集計関数です。

MIN() 関数は、値の集合から最小値を返します。

## Analyzeの構文

```python
func.min(<column>)
```

## Analyzeの例

```python
table.station_id, func.min(table.price).alias('min_price')

| station_id | min_price |
|------------|-----------|
|     1      |   3.45    |
```

## SQLの構文

```sql
MIN(<expr>)
```

## 引数

| 引数 | 説明    |
|-----------|----------------|
| `<expr>`  | 任意の式 |

## 戻り値の型

最小値。その値の型で返されます。

## SQLの例

---
title: MIN
---

集計関数です。

MIN() 関数は、値の集合から最小値を返します。

## SQLの構文

```sql
MIN(expression)
```

## 引数

| 引数   | 説明 |
| ----------- | ----------- |
| expression  | 任意の式 |

## 戻り値の型

最小値。その値の型で返されます。

## SQLの例

**テーブルの作成とサンプルデータの挿入**
```sql
CREATE TABLE gas_prices (
  id INT,
  station_id INT,
  price FLOAT
);

INSERT INTO gas_prices (id, station_id, price)
VALUES (1, 1, 3.50),
       (2, 1, 3.45),
       (3, 1, 3.55),
       (4, 2, 3.40),
       (5, 2, 3.35);
```

**クエリのデモ: ステーション 1 の最低ガソリン価格を求める**
```sql
SELECT station_id, MIN(price) AS min_price
FROM gas_prices
WHERE station_id = 1
GROUP BY station_id;
```

**結果**
```sql
| station_id | min_price |
|------------|-----------|
|     1      |   3.45    |
```
