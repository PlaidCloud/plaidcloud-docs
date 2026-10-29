---
title: JQ (Lakehouse v1)
description: JQ — JQ関数は、jqを適用できる集合を返すSQL関数です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/jq.md
---

JQ関数は、Variant列に格納されたJSONデータに[jq](https://jqlang.github.io/jq/)フィルターを適用できる、集合を返すSQL関数です。この関数を使うと、指定したjqフィルターを適用してJSONデータを処理し、結果を行の集合として返すことができます。

## SQL構文

```sql
JQ (<jq_expression>, <json_data>)
```

| パラメーター       | 説明                                                                                                                                                                                                                                                                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `jq_expression` | `jq` 構文を使ってJSONデータの処理方法と変換方法を定義する、`jq` フィルター式です。この式では、JSONオブジェクトや配列内のデータを選択、変更、操作する方法を指定できます。jqがサポートする構文、フィルター、関数については、[jq Manual](https://jqlang.github.io/jq/manual/#basic-filters)を参照してください。 |
| `json_data`     | `jq` フィルター式で処理または変換するJSON形式の入力です。JSONオブジェクト、配列、その他の有効なJSONデータ構造を指定できます。                                                                                                                                                                                          |

## 戻り値の型

JQ関数は、JSON値の集合を返します。各値は、`<jq_expression>` に基づいて変換または抽出された結果の要素に対応します。

## SQLの例

まず、`id` 列と `profile` 列を持つ `customer_data` という名前のテーブルを作成します。`profile` は、ユーザー情報を格納するJSON型です。

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

次の例では、JSONデータから特定のフィールドを抽出します。

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

次の例では、ユーザーIDと、各ユーザーの年齢に1を加えた値を選択します。

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

次の例では、都市名を大文字に変換します。

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
