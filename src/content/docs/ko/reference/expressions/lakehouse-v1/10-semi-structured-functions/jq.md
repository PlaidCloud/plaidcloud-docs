---
title: JQ (Lakehouse v1)
description: JQ — JQ 함수는 jq를 적용할 수 있는 집합 반환 SQL 함수입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/jq.md
---

JQ 함수는 Variant 열에 저장된 JSON 데이터에 [jq](https://jqlang.github.io/jq/) 필터를 적용할 수 있는 집합 반환 SQL 함수입니다. 이 함수로 지정한 jq 필터를 적용해 JSON 데이터를 처리하고, 결과를 행 집합으로 반환합니다.

## SQL Syntax

```sql
JQ (<jq_expression>, <json_data>)
```

| 매개변수       | 설명                                                                                                                                                                                                                                                                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `jq_expression` | `jq` 구문을 사용해 JSON 데이터를 처리하고 변환하는 방법을 정의하는 `jq` 필터 식입니다. 이 식으로 JSON 객체와 배열 안의 데이터를 선택, 수정, 조작하는 방법을 지정할 수 있습니다. jq가 지원하는 구문, 필터, 함수에 대한 자세한 내용은 [jq Manual](https://jqlang.github.io/jq/manual/#basic-filters)을 참조하십시오. |
| `json_data`     | `jq` 필터 식으로 처리하거나 변환하려는 JSON 형식의 입력입니다. JSON 객체, 배열 또는 유효한 모든 JSON 데이터 구조일 수 있습니다.                                                                                                                                                                                          |

## 반환 타입

JQ 함수는 JSON 값의 집합을 반환하며, 각 값은 `<jq_expression>`에 따라 변환되거나 추출된 결과의 요소에 해당합니다.

## SQL Examples

먼저 `id`와 `profile` 열이 있는 `customer_data` 테이블을 만듭니다. `profile`은 사용자 정보를 저장하는 JSON 타입입니다.

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

이 예제는 JSON 데이터에서 특정 필드를 추출합니다.

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

이 예제는 각 사용자의 ID와 1만큼 증가시킨 나이를 선택합니다.

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

이 예제는 도시 이름을 대문자로 변환합니다.

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
