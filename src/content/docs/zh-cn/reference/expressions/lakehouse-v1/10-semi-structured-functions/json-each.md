---
title: JSON_EACH（Lakehouse v1）
description: JSON_EACH — 从 JSON 对象中提取键值对，将结构拆分为结果集中的单独行。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-each.md
---

从 JSON 对象中提取键值对，将结构拆分为结果集中的单独行。每一行表示由输入 JSON 表达式得出的一个不同的键值对。

## Analyze 语法

```python
func.json_each(<json_string>)
```

## Analyze 示例

```python

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.json_each(func.parse_json('{"name": "john", "age": 25, "isstudent": false, "grades": [90, 85, 92]}')) │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ ('age','25')                                                                                               │
│ ('grades','[90,85,92]')                                                                                    │
│ ('isStudent','false')                                                                                      │
│ ('name','"John"')                                                                                          │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
JSON_EACH(<json_string>)
```

## 返回类型

JSON_EACH 返回一组元组，每个元组由一个 STRING 键和对应的 VARIANT 值组成。

## SQL 示例

```sql
-- Extract key-value pairs from a JSON object representing information about a person
SELECT
  JSON_EACH(
    PARSE_JSON (
      '{"name": "John", "age": 25, "isStudent": false, "grades": [90, 85, 92]}'
    )
  );


┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ json_each(parse_json('{"name": "john", "age": 25, "isstudent": false, "grades": [90, 85, 92]}')) │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ ('age','25')                                                                                     │
│ ('grades','[90,85,92]')                                                                          │
│ ('isStudent','false')                                                                            │
│ ('name','"John"')                                                                                │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘

-- Display data types of the extracted values
SELECT
  TYPEOF (
    JSON_EACH(
      PARSE_JSON (
        '{"name": "John", "age": 25, "isStudent": false, "grades": [90, 85, 92]}'
      )
    )
  );

┌──────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ typeof(json_each(parse_json('{"name": "john", "age": 25, "isstudent": false, "grades": [90, 85, 92]}'))) │
├──────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ TUPLE(STRING, VARIANT) NULL                                                                              │
│ TUPLE(STRING, VARIANT) NULL                                                                              │
│ TUPLE(STRING, VARIANT) NULL                                                                              │
│ TUPLE(STRING, VARIANT) NULL                                                                              │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
