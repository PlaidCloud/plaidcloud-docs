---
title: JSON_PATH_QUERY_ARRAY（Lakehouse v1）
description: JSON_PATH_QUERY_ARRAY — 获取 JSON 路径对指定 JSON 值返回的所有 JSON 项。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-path-query-array.md
---

获取 JSON 路径对指定 JSON 值返回的所有 JSON 项，并将结果包装为数组。

## Analyze 语法

```python
func.json_path_query_array(<variant>, <path_name>)
```

## Analyze 示例

```python
table.name, func.json_path_query_array(table.details, '$.features.*').alias('all_features')

   name     |     all_features
------------+-----------------------
 Laptop     | ["16GB", "512GB"]
 Smartphone | ["4GB", "128GB"]
 Headphones | ["20h", "5.0"]
```

## SQL 语法

```sql
JSON_PATH_QUERY_ARRAY(<variant>, '<path_name>')
```


## 返回类型

VARIANT

## SQL 示例

**创建表并插入示例数据**

```sql
CREATE TABLE products (
    name VARCHAR,
    details VARIANT
);

INSERT INTO products (name, details)
VALUES ('Laptop', '{"brand": "Dell", "colors": ["Black", "Silver"], "price": 1200, "features": {"ram": "16GB", "storage": "512GB"}}'),
       ('Smartphone', '{"brand": "Apple", "colors": ["White", "Black"], "price": 999, "features": {"ram": "4GB", "storage": "128GB"}}'),
       ('Headphones', '{"brand": "Sony", "colors": ["Black", "Blue", "Red"], "price": 150, "features": {"battery": "20h", "bluetooth": "5.0"}}');
```

**查询演示：将产品详情中的所有特性提取为数组**

```sql
SELECT
    name,
    JSON_PATH_QUERY_ARRAY(details, '$.features.*') AS all_features
FROM
    products;
```

**结果**

```text
   name    |         all_features
-----------+-----------------------
 Laptop    | ["16GB", "512GB"]
 Smartphone | ["4GB", "128GB"]
 Headphones | ["20h", "5.0"]
```
