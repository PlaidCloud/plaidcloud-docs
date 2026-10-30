---
title: SKEWNESS (Lakehouse v1)
description: SKEWNESS：返回所有输入值的偏度（分布的不对称程度）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-skewness.md
---

聚合函数。

`SKEWNESS()` 函数返回所有输入值的偏度。

## Analyze 语法

```python
func.skewness(<expr>)
```

## Analyze 示例

```python
func.skewness(table.temperature).alias('temperature_skewness')

| temperature_skewness |
|----------------------|
|      0.68            |
```

## SQL 语法

```sql
SKEWNESS(<expr>)
```

## 参数

| 参数 | 说明                     |
|-----------| -----------                     |
| `<expr>`  | 任意数值表达式        |

## 返回类型

可为空的 Float64。

## SQL 示例

**创建表并插入示例数据**
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

**查询演示：计算温度数据的偏度**

```sql
SELECT SKEWNESS(temperature) AS temperature_skewness
FROM temperature_data;
```

**结果**
```sql
| temperature_skewness |
|----------------------|
|      0.68            |
```
