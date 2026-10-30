---
title: ARG_MAX (Lakehouse v1)
description: ARG_MAX — val の最大値に対応する arg の値を計算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-arg-max.md
---

`val` の最大値に対応する `arg` の値を計算します。`val` の最大値に対して `arg` の値が複数ある場合は、最初に見つかった値を返します。

## Analyzeの構文

```python
func.arg_max(<expr>)
```

## Analyzeの例

```python
func.arg_max(table.product, table.price).alias('max_price_product')

| max_price_product |
| ----------------- |
| Product C         |
```

## SQLの構文

```sql
ARG_MAX(<arg>, <val>)
```

## 引数

| 引数 | 説明 |
|-----------|---------------------------------------------------------------------------------------------------|
| `<arg>`   | PlaidCloud Lakehouse がサポートする任意のデータ型の引数 |
| `<val>`   | PlaidCloud Lakehouse がサポートする任意のデータ型の値 |

## 戻り値の型

`val` の最大値に対応する `arg` の値。

 `arg` の型と一致します。

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

**クエリ: ARG_MAX() 関数を使用する**

ARG_MAX() 関数を使用して、価格が最大の製品を求めます。
```sql
SELECT ARG_MAX(product, price) AS max_price_product
FROM sales;
```

結果は次のようになります。
```sql
| max_price_product |
| ----------------- |
| Product C         |
```
