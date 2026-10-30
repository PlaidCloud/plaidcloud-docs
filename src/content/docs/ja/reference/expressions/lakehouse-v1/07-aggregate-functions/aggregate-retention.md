---
title: RETENTION (Lakehouse v1)
description: RETENTION — 集計関数です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-retention.md
---

集計関数です。

RETENTION() 関数は、1 個から 32 個までの UInt8 型の条件を引数として受け取ります。各条件は、イベントで特定の条件が満たされたかどうかを示します。

任意の条件を引数として指定できます（WHERE と同様）。

最初の条件を除く各条件は、最初の条件と組み合わせて評価されます。2 番目の結果は、最初と 2 番目が真の場合に真となり、3 番目の結果は、最初と 3 番目が真の場合に真となります。以降も同様です。

## Analyzeの構文

```python
func.retention(<cond1> , <cond2> , ..., <cond32>)
```

## Analyzeの例

```python
table.user_id, func.retention(table.event_type=='signup', table.event_type='login', table.event_type='purchase').alias('sales_amounts')

| user_id | retention |
|---------|-----------|
|   1     | [1, 1, 0] |
|   2     | [1, 0, 1] |
|   3     | [1, 1, 0] |
```

## SQLの構文

```sql
RETENTION( <cond1> , <cond2> , ..., <cond32> );
```

## 引数

| 引数 | 説明                                 |
|-----------|---------------------------------------------|
| `<cond>`  | ブール値の結果を返す式 |

## 戻り値の型

1 または 0 の配列。

## SQLの例

**テーブルの作成とサンプルデータの挿入**
```sql
CREATE TABLE user_events (
  id INT,
  user_id INT,
  event_date DATE,
  event_type VARCHAR
);

INSERT INTO user_events (id, user_id, event_date, event_type)
VALUES (1, 1, '2022-01-01', 'signup'),
       (2, 1, '2022-01-02', 'login'),
       (3, 2, '2022-01-01', 'signup'),
       (4, 2, '2022-01-03', 'purchase'),
       (5, 3, '2022-01-01', 'signup'),
       (6, 3, '2022-01-02', 'login');
```

**クエリのデモ: サインアップ、ログイン、購入のイベントに基づいてユーザーのリテンションを計算する**
```sql
SELECT
  user_id,
  RETENTION(event_type = 'signup', event_type = 'login', event_type = 'purchase') AS retention
FROM user_events
GROUP BY user_id;
```

**結果**
```sql
| user_id | retention |
|---------|-----------|
|   1     | [1, 1, 0] |
|   2     | [1, 0, 1] |
|   3     | [1, 1, 0] |
```
