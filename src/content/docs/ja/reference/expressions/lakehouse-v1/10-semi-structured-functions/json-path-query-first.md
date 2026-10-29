---
title: JSON_PATH_QUERY_FIRST (Lakehouse v1)
description: JSON_PATH_QUERY_FIRST — 指定したJSON値に対してJSONパスが返す最初のJSON項目を取得します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-path-query-first.md
---

指定したJSON値に対してJSONパスが返す最初のJSON項目を取得します。


## Analyze構文

```python
func.json_path_query_first(<variant>, <path_name>)
```

## Analyzeの例

```python
table.name, func.json_path_query_first(table.details, '$.features.*').alias('first_feature')

┌────────────┬───────────────┐
│ name       │ first_feature │
├────────────┼───────────────┤
│ Laptop     │ "16GB"        │
│ Laptop     │ "16GB"        │
│ Smartphone │ "4GB"         │
│ Smartphone │ "4GB"         │
│ Headphones │ "20h"         │
│ Headphones │ "20h"         │
└────────────┴───────────────┘
```

## SQL構文

```sql
JSON_PATH_QUERY_FIRST(<variant>, '<path_name>')
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

**クエリのデモ：製品詳細から最初の特徴を抽出する**

```sql
SELECT
    name,
    JSON_PATH_QUERY(details, '$.features.*') AS all_features,
    JSON_PATH_QUERY_FIRST(details, '$.features.*') AS first_feature
FROM
    products;
```

**結果**

```sql
┌────────────┬──────────────┬───────────────┐
│ name       │ all_features │ first_feature │
├────────────┼──────────────┼───────────────┤
│ Laptop     │ "16GB"       │ "16GB"        │
│ Laptop     │ "512GB"      │ "16GB"        │
│ Smartphone │ "4GB"        │ "4GB"         │
│ Smartphone │ "128GB"      │ "4GB"         │
│ Headphones │ "20h"        │ "20h"         │
│ Headphones │ "5.0"        │ "20h"         │
└────────────┴──────────────┴───────────────┘
```
