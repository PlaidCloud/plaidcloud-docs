---
title: MIN (Lakehouse v1)
description: MIN：返回一组值中的最小值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-min.md
---

聚合函数。

MIN() 函数返回一组值中的最小值。

## Analyze 语法

```python
func.min(<column>)
```

## Analyze 示例

```python
table.station_id, func.min(table.price).alias('min_price')

| station_id | min_price |
|------------|-----------|
|     1      |   3.45    |
```

## SQL 语法

```sql
MIN(<expr>)
```

## 参数

| 参数 | 说明    |
|-----------|----------------|
| `<expr>`  | 任意表达式 |

## 返回类型

最小值，类型与该值的类型相同。

## SQL 示例

---
title: MIN
---

聚合函数。

MIN() 函数返回一组值中的最小值。

## SQL 语法

```sql
MIN(expression)
```

## 参数

| 参数   | 说明 |
| ----------- | ----------- |
| expression  | 任意表达式 |

## 返回类型

最小值，类型与该值的类型相同。

## SQL 示例

**创建表并插入示例数据**
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

**查询演示：查找 1 号加油站的最低油价**
```sql
SELECT station_id, MIN(price) AS min_price
FROM gas_prices
WHERE station_id = 1
GROUP BY station_id;
```

**结果**
```sql
| station_id | min_price |
|------------|-----------|
|     1      |   3.45    |
```
