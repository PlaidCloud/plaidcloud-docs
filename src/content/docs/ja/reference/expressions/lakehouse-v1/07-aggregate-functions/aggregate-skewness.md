---
title: SKEWNESS (Lakehouse v1)
description: SKEWNESS — すべての入力値の歪度（分布の非対称性）を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-skewness.md
---

集計関数です。

`SKEWNESS()` 関数は、すべての入力値の歪度を返します。

## Analyzeの構文

```python
func.skewness(<expr>)
```

## Analyzeの例

```python
func.skewness(table.temperature).alias('temperature_skewness')

| temperature_skewness |
|----------------------|
|      0.68            |
```

## SQLの構文

```sql
SKEWNESS(<expr>)
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
CREATE TABLE temperature_data (
                                  id INT,
                                  city_id INT,
                                  temperature FLOAT
);

INSERT INTO temperature_data (id, city_id, temperature)
VALUES (1, 1, 60),
       (2, 1, 65),
       (3, 1, 62),
       (4, 2, 70),
       (5, 2, 75);
```

**クエリのデモ: 気温データの歪度を計算する**

```sql
SELECT SKEWNESS(temperature) AS temperature_skewness
FROM temperature_data;
```

**結果**
```sql
| temperature_skewness |
|----------------------|
|      0.68            |
```
