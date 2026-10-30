---
title: APPROX_COUNT_DISTINCT (Lakehouse v1)
description: APPROX_COUNT_DISTINCT — HyperLogLog アルゴリズムを使用して、データセット内の一意な値の数を推定します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-approx-count-distinct.md
---

[HyperLogLog](https://en.wikipedia.org/wiki/HyperLogLog) アルゴリズムを使用して、データセット内の一意な値の数を推定します。

HyperLogLog アルゴリズムは、少ないメモリと時間で一意な要素数の近似値を提供します。推定値で問題ない大規模なデータセットを扱う場合に、この関数の利用を検討してください。精度と引き換えに、一意な値の数を高速かつ効率的に返す方法です。

正確な結果を得るには、[COUNT_DISTINCT](../aggregate-count-distinct)を使用してください。詳しくは[例](#sqlの例)をご覧ください。

## Analyzeの構文

```python
func.approx_count_distinct(<expr>)
```

## Analyzeの例

```python
func.approx_count_distinct(table.user_id).alias('approx_distinct_user_count')

| approx_distinct_user_count |
|----------------------------|
|             4              |
```

## SQLの構文

```sql
APPROX_COUNT_DISTINCT(<expr>)
```

## 戻り値の型

整数。

## SQLの例

**テーブルの作成とサンプルデータの挿入**
```sql
CREATE TABLE user_events (
  id INT,
  user_id INT,
  event_name VARCHAR
);

INSERT INTO user_events (id, user_id, event_name)
VALUES (1, 1, 'Login'),
       (2, 2, 'Login'),
       (3, 3, 'Login'),
       (4, 1, 'Logout'),
       (5, 2, 'Logout'),
       (6, 4, 'Login'),
       (7, 1, 'Login');
```

**クエリのデモ: 一意なユーザー ID の数を推定する**
```sql
SELECT APPROX_COUNT_DISTINCT(user_id) AS approx_distinct_user_count
FROM user_events;
```

**結果**
```sql
| approx_distinct_user_count |
|----------------------------|
|             4              |
```
