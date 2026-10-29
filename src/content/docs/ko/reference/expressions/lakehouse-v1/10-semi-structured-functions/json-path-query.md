---
title: JSON_PATH_QUERY (Lakehouse v1)
description: JSON_PATH_QUERY — 지정한 JSON에 대해 JSON 경로가 반환하는 모든 JSON 항목을 가져옵니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-path-query.md
---

지정한 JSON 값에 대해 JSON 경로가 반환하는 모든 JSON 항목을 가져옵니다.

## Analyze Syntax

```python
func.json_path_query(<variant>, <path_name>)
```

## Analyze Examples

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

## SQL Syntax

```sql
JSON_PATH_QUERY(<variant>, '<path_name>')
```


## 반환 타입

VARIANT

## SQL Examples

**테이블을 만들고 샘플 데이터 삽입**

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

**쿼리 데모: 제품 세부 정보의 모든 기능 추출**

```sql
SELECT
    name,
    JSON_PATH_QUERY(details, '$.features.*') AS all_features
FROM
    products;
```

**결과**

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
