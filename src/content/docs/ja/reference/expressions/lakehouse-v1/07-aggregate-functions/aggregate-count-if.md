---
title: COUNT_IF (Lakehouse v1)
description: COUNT_IF — 接尾辞 _IF は、任意の集計関数の名前に付加できます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-count-if.md
---

接尾辞 `_IF` は、任意の集計関数の名前に付加できます。この場合、集計関数は追加の引数として条件を受け取ります。

## Analyzeの構文

```python
func.count_if(<column>, <cond>)
```

## Analyzeの例

```python
func.count_if(table.status, table.status=='Completed').alias('completed_orders')

| completed_orders |
|------------------|
|        3         |
```

## SQLの例
```sql
COUNT_IF(<column>, <cond>)
```

## SQLの例

**テーブルの作成とサンプルデータの挿入**
```sql
CREATE TABLE orders (
  id INT,
  customer_id INT,
  status VARCHAR,
  total FLOAT
);

INSERT INTO orders (id, customer_id, status, total)
VALUES (1, 1, 'completed', 100),
       (2, 2, 'completed', 200),
       (3, 1, 'pending', 150),
       (4, 3, 'completed', 250),
       (5, 2, 'pending', 300);
```

**クエリのデモ: 完了した注文をカウントする**
```sql
SELECT COUNT_IF(status, status = 'completed') AS completed_orders
FROM orders;
```

**結果**
```sql
| completed_orders |
|------------------|
|        3         |
```
