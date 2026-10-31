---
title: MAX (Lakehouse v1)
description: MAX — 値の集合から最大値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-max.md
---

集計関数です。

MAX() 関数は、値の集合から最大値を返します。

## Analyzeの構文

```python
func.max(<column>)
```

## Analyzeの例

```python
table.city, func.max(table.temperature).alias('max_temperature')

|    city    | max_temperature |
|------------|-----------------|
| New York   |       32        |
```

## SQLの構文

```sql
MAX(<expr>)
```

## 引数

| 引数 | 説明 |
|-----------| ----------- |
| `<expr>`  | 任意の式 |

## 戻り値の型

最大値。その値の型で返されます。

## SQLの例

**テーブルの作成とサンプルデータの挿入**
```sql
CREATE TABLE temperatures (
  id INT,
  city VARCHAR,
  temperature FLOAT
);

INSERT INTO temperatures (id, city, temperature)
VALUES (1, 'New York', 30),
       (2, 'New York', 28),
       (3, 'New York', 32),
       (4, 'Los Angeles', 25),
       (5, 'Los Angeles', 27);
```

**クエリのデモ: ニューヨーク市の最高気温を求める**

```sql
SELECT city, MAX(temperature) AS max_temperature
FROM temperatures
WHERE city = 'New York'
GROUP BY city;
```

**結果**
```sql
|    city    | max_temperature |
|------------|-----------------|
| New York   |       32        |
```
