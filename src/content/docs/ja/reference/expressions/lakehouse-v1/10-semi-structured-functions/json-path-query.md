---
title: JSON_PATH_QUERY (Lakehouse v1)
description: JSON_PATH_QUERY — 指定したJSON値に対してJSONパスが返すすべてのJSON項目を取得します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-path-query.md
---

指定したJSON値に対してJSONパスが返すすべてのJSON項目を取得します。

## Analyze構文

```python
func.json_path_query(<variant>, <path_name>)
```

## Analyzeの例

```python
table.name, func.json_path_query(table.details, '$.features.*').alias('all_features')

┌────────────┬──────────────┐
│ name       │ all_features │
├────────────┼──────────────┤
│ Laptop     │ "16GB"       │
│ Laptop     │ "512GB"      │
│ Smartphone │ "4GB"        │
│ Smartphone │ "128GB"      │
│ Headphones │ "20h"        │
│ Headphones │ "5.0"        │
└────────────┴──────────────┘
```

## SQL構文

```sql
JSON_PATH_QUERY(<variant>, '<path_name>')
```


## 戻り値の型

VARIANT

## SQLの例

**テーブルの作成とサンプルデータの挿入**

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

**クエリのデモ：製品詳細からすべての特徴を抽出する**

```sql
SELECT
    name,
    JSON_PATH_QUERY(details, '$.features.*') AS all_features
FROM
    products;
```

**結果**

```sql
┌────────────┬──────────────┐
│ name       │ all_features │
├────────────┼──────────────┤
│ Laptop     │ "16GB"       │
│ Laptop     │ "512GB"      │
│ Smartphone │ "4GB"        │
│ Smartphone │ "128GB"      │
│ Headphones │ "20h"        │
│ Headphones │ "5.0"        │
└────────────┴──────────────┘
```
