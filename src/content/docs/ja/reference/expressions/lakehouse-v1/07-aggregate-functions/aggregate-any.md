---
title: ANY (Lakehouse v1)
description: ANY — 集合内で最初に見つかった NULL ではない値を返します。実行順序が変わる場合、結果は不定です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-any.md
---

集計関数です。

ANY() 関数は、最初に見つかった（NULL ではない）値を選択します。ただし、その列のすべての行が NULL の場合は NULL を返します。クエリは任意の順序で実行される可能性があり、実行のたびに順序が変わることもあるため、この関数の結果は不定です。確定的な結果を得るには、'any' の代わりに 'min' または 'max' 関数を使用してください。

## Analyzeの構文

```python
func.any(<expr>)
```

## Analyzeの例

```python
func.any(table.product_name).alias('any_product_name')

| any_product_name |
|------------------|
| Laptop           |
```

## SQLの構文

```sql
ANY(<expr>)
```

## 引数

| 引数 | 説明 |
|-----------|----------------|
| `<expr>`  | 任意の式 |

## 戻り値の型

最初に見つかった（NULL ではない）値で、その値の型で返されます。すべての値が NULL の場合、戻り値は NULL です。

## SQLの例

**テーブルの作成とサンプルデータの挿入**
```sql
CREATE TABLE product_data (
  id INT,
  product_name VARCHAR NULL,
  price FLOAT NULL
);

INSERT INTO product_data (id, product_name, price)
VALUES (1, 'Laptop', 1000),
       (2, NULL, 800),
       (3, 'Keyboard', NULL),
       (4, 'Mouse', 25),
       (5, 'Monitor', 150);
```

**クエリのデモ: 最初に見つかった NULL ではない製品名を取得する**
```sql
SELECT ANY(product_name) AS any_product_name
FROM product_data;
```

**結果**
```sql
| any_product_name |
|------------------|
| Laptop           |
```
