---
title: JQ（Lakehouse v1）
description: JQ — JQ 函数是一个返回集合的 SQL 函数，可用于应用 jq。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/jq.md
---

JQ 函数是一个返回集合的 SQL 函数，可将 [jq](https://jqlang.github.io/jq/) 筛选器应用于存储在 Variant 列中的 JSON 数据。使用此函数，可通过应用指定的 jq 筛选器处理 JSON 数据，并将结果作为一组行返回。

## SQL 语法

```sql
JQ (<jq_expression>, <json_data>)
```

| 参数            | 说明 |
|-----------------|------|
| `jq_expression` | `jq` 筛选器表达式，使用 `jq` 语法定义如何处理和转换 JSON 数据。该表达式可指定如何选择、修改和操作 JSON 对象和数组中的数据。有关 jq 支持的语法、筛选器和函数的信息，请参阅 [jq 手册](https://jqlang.github.io/jq/manual/#basic-filters)。 |
| `json_data`     | 要使用 `jq` 筛选器表达式处理或转换的 JSON 格式输入。可以是 JSON 对象、数组或任何有效的 JSON 数据结构。 |

## 返回类型

JQ 函数返回一组 JSON 值，其中每个值对应根据 `<jq_expression>` 转换或提取的结果中的一个元素。

## SQL 示例

首先，创建名为 `customer_data` 的表，包含 `id` 和 `profile` 列，其中 `profile` 为 JSON 类型，用于存储用户信息：

```sql
CREATE TABLE customer_data (
    id INT,
    profile JSON
);

INSERT INTO customer_data VALUES
    (1, '{"name": "Alice", "age": 30, "city": "New York"}'),
    (2, '{"name": "Bob", "age": 25, "city": "Los Angeles"}'),
    (3, '{"name": "Charlie", "age": 35, "city": "Chicago"}');
```

此示例从 JSON 数据中提取指定字段：

```sql
SELECT
    id,
    jq('.name', profile) AS customer_name
FROM
    customer_data;

┌─────────────────────────────────────┐
│        id       │   customer_name   │
├─────────────────┼───────────────────┤
│               1 │ "Alice"           │
│               2 │ "Bob"             │
│               3 │ "Charlie"         │
└─────────────────────────────────────┘
```

此示例选择用户 ID 以及每位用户加 1 后的年龄：

```sql
SELECT
    id,
    jq('.age + 1', profile) AS updated_age
FROM
    customer_data;

┌─────────────────────────────────────┐
│        id       │    updated_age    │
├─────────────────┼───────────────────┤
│               1 │ 31                │
│               2 │ 26                │
│               3 │ 36                │
└─────────────────────────────────────┘
```

此示例将城市名称转换为大写：

```sql
SELECT
    id,
    jq('.city | ascii_upcase', profile) AS city_uppercase
FROM
    customer_data;

┌─────────────────────────────────────┐
│        id       │   city_uppercase  │
├─────────────────┼───────────────────┤
│               1 │ "NEW YORK"        │
│               2 │ "LOS ANGELES"     │
│               3 │ "CHICAGO"         │
└─────────────────────────────────────┘
```
