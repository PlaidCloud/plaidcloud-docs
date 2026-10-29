---
title: MAX (Lakehouse v1)
description: MAX：返回一组值中的最大值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-max.md
---

聚合函数。

MAX() 函数返回一组值中的最大值。

## Analyze 语法

```python
func.max(<column>)
```

## Analyze 示例

```python
table.city, func.max(table.temperature).alias('max_temperature')

|    city    | max_temperature |
|------------|-----------------|
| New York   |       32        |
```

## SQL 语法

```sql
MAX(<expr>)
```

## 参数

| 参数 | 说明 |
|-----------| ----------- |
| `<expr>`  | 任意表达式 |

## 返回类型

最大值，类型与该值的类型相同。

## SQL 示例

**创建表并插入示例数据**
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

**查询演示：查找纽约市的最高温度**

```sql
SELECT city, MAX(temperature) AS max_temperature
FROM temperatures
WHERE city = 'New York'
GROUP BY city;
```

**结果**
```sql
|    city    | max_temperature |
|------------|-----------------|
| New York   |       32        |
```
