---
title: ANY (Lakehouse v1)
description: ANY：返回一组值中第一个遇到的非 NULL 值；执行顺序变化时结果不确定。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-any.md
---

聚合函数。

ANY() 函数选取第一个遇到的（非 NULL）值，除非该列所有行的值均为 NULL。查询可以按任意顺序执行，甚至每次执行顺序都不同，因此该函数的结果是不确定的。若要获得确定的结果，可以改用 'min' 或 'max' 函数代替 'any'。

## Analyze 语法

```python
func.any(<expr>)
```

## Analyze 示例

```python
func.any(table.product_name).alias('any_product_name')

| any_product_name |
|------------------|
| Laptop           |
```

## SQL 语法

```sql
ANY(<expr>)
```

## 参数

| 参数 | 说明 |
|-----------|----------------|
| `<expr>`  | 任意表达式 |

## 返回类型

第一个遇到的（非 NULL）值，类型与该值的类型相同。如果所有值均为 NULL，则返回 NULL。

## SQL 示例

**创建表并插入示例数据**
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

**查询演示：检索第一个遇到的非 NULL 产品名称**
```sql
SELECT ANY(product_name) AS any_product_name
FROM product_data;
```

**结果**
```sql
| any_product_name |
|------------------|
| Laptop           |
```
