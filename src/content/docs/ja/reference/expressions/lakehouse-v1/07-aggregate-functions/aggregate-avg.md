---
title: AVG (Lakehouse v1)
description: AVG — 式の平均値を返します。NULL 値は無視されます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-avg.md
---

集計関数です。

AVG() 関数は、式の平均値を返します。

**注記：** NULL 値はカウントされません。


## Analyzeの構文

```python
func.avg(<column>)
```

## Analyzeの例

```python
func.avg(table.price).alias('avg_price')

| avg_price |
| --------- |
| 20.4      |
```

## SQLの構文

```sql
AVG(<expr>)
```

## 引数

| 引数 | 説明 |
|-----------|--------------------------|
| `<expr>`  | 任意の数値式 |

## 戻り値の型

double

## SQLの例

**テーブルの作成とサンプルデータの挿入**

"sales" という名前のテーブルを作成し、サンプルデータを挿入します。
```sql
CREATE TABLE sales (
  id INTEGER,
  product VARCHAR(50),
  price FLOAT
);

INSERT INTO sales (id, product, price)
VALUES (1, 'Product A', 10.5),
       (2, 'Product B', 20.75),
       (3, 'Product C', 30.0),
       (4, 'Product D', 15.25),
       (5, 'Product E', 25.5);
```

**クエリ: AVG() 関数を使用する**

AVG() 関数を使用して、"sales" テーブル内のすべての製品の平均価格を求めます。
```sql
SELECT AVG(price) AS avg_price
FROM sales;
```

結果は次のようになります。
```sql
| avg_price |
| --------- |
| 20.4      |
```
