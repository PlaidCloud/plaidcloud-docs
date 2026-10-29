---
title: SUM_IF (Lakehouse v1)
description: SUM_IF — 接尾辞 -If は、任意の集計関数の名前に付加できます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-sum-if.md
---

接尾辞 -If は、任意の集計関数の名前に付加できます。この場合、集計関数は追加の引数として条件を受け取ります。

## Analyzeの構文

```python
func.sum_if(<column>, <cond>)
```

## Analyzeの例

```python
func.sum_if(table.amount, table.status=='Completed').alias('total_amount_completed')

| total_amount_completed |
|------------------------|
|         270.0          |
```

## SQLの構文

```sql
SUM_IF(<column>, <cond>)
```

## SQLの例

**テーブルの作成とサンプルデータの挿入**
```sql
CREATE TABLE order_data (
  id INT,
  customer_id INT,
  amount FLOAT,
  status VARCHAR
);

INSERT INTO order_data (id, customer_id, amount, status)
VALUES (1, 1, 100, 'Completed'),
       (2, 2, 50, 'Completed'),
       (3, 3, 80, 'Cancelled'),
       (4, 4, 120, 'Completed'),
       (5, 5, 75, 'Cancelled');
```

**クエリのデモ: 完了した注文の合計金額を計算する**
```sql
SELECT SUM_IF(amount, status = 'Completed') AS total_amount_completed
FROM order_data;
```

**結果**
```sql
| total_amount_completed |
|------------------------|
|         270.0          |
```
