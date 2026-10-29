---
title: JSON_PATH_MATCH (Lakehouse v1)
description: JSON_PATH_MATCH — 指定したJSONパス式が、JSONデータ内の特定の条件に一致するかどうかをチェックします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-path-match.md
---

指定したJSONパス式が、JSONデータ内の特定の条件に一致するかどうかをチェックします。ご注意：`@@` 演算子はこの関数と同義です。詳細については、JSON演算子を参照してください。


## Analyze構文

```python
func.json_path_match(<json_data>, <json_path_expression)
```

## Analyzeの例

```python
func.json_path_match(func.parse_json('{"a":1,"b":[1,2,3]}'), '$.a == 1')
┌──────────────────────────────────────────────────────────────────────────┐
│ func.json_path_match(func.parse_json('{"a":1,"b":[1,2,3]}'), '$.a == 1') │
├──────────────────────────────────────────────────────────────────────────┤
│ true                                                                     │
└──────────────────────────────────────────────────────────────────────────┘

func.json_path_match(func.parse_json('{"a":1,"b":[1,2,3]}'), '$.b[0] > 1')
┌────────────────────────────────────────────────────────────────────────────┐
│ func.json_path_match(func.parse_json('{"a":1,"b":[1,2,3]}'), '$.b[0] > 1') │
├────────────────────────────────────────────────────────────────────────────┤
│ false                                                                      │
└────────────────────────────────────────────────────────────────────────────┘
```

## SQL構文

```sql
JSON_PATH_MATCH(<json_data>, <json_path_expression>)
```

- `json_data`: 調べるJSONデータを指定します。JSONオブジェクトまたは配列を指定できます。
- `json_path_expression`: JSONデータ内でチェックする条件を指定します。この式は、一致させる特定のパスや基準を表し、たとえばJSON構造内の特定のフィールド値が一定の条件を満たしているかどうかを検証します。`$` 記号はJSONデータのルートを表します。パス式の先頭に使用し、JSON構造の最上位のオブジェクトを示します。

## 戻り値の型

この関数は次の値を返します。

- 指定したJSONパス式がJSONデータ内の条件に一致する場合は `true`
- 指定したJSONパス式がJSONデータ内の条件に一致しない場合は `false`
- `json_data` または `json_path_expression` のいずれかがNULLまたは無効な場合は NULL

## SQLの例

```sql
-- Check if the value at JSON path $.a is equal to 1
SELECT JSON_PATH_MATCH(parse_json('{"a":1,"b":[1,2,3]}'), '$.a == 1');

┌────────────────────────────────────────────────────────────────┐
│ json_path_match(parse_json('{"a":1,"b":[1,2,3]}'), '$.a == 1') │
├────────────────────────────────────────────────────────────────┤
│ true                                                           │
└────────────────────────────────────────────────────────────────┘

-- Check if the first element in the array at JSON path $.b is greater than 1
SELECT JSON_PATH_MATCH(parse_json('{"a":1,"b":[1,2,3]}'), '$.b[0] > 1');

┌──────────────────────────────────────────────────────────────────┐
│ json_path_match(parse_json('{"a":1,"b":[1,2,3]}'), '$.b[0] > 1') │
├──────────────────────────────────────────────────────────────────┤
│ false                                                            │
└──────────────────────────────────────────────────────────────────┘

-- Check if any element in the array at JSON path $.b
-- from the second one to the last are greater than or equal to 2
SELECT JSON_PATH_MATCH(parse_json('{"a":1,"b":[1,2,3]}'), '$.b[1 to last] >= 2');

┌───────────────────────────────────────────────────────────────────────────┐
│ json_path_match(parse_json('{"a":1,"b":[1,2,3]}'), '$.b[1 to last] >= 2') │
├───────────────────────────────────────────────────────────────────────────┤
│ true                                                                      │
└───────────────────────────────────────────────────────────────────────────┘

-- NULL is returned if either the json_data or json_path_expression is NULL or invalid.
SELECT JSON_PATH_MATCH(parse_json('{"a":1,"b":[1,2,3]}'), NULL);

┌──────────────────────────────────────────────────────────┐
│ json_path_match(parse_json('{"a":1,"b":[1,2,3]}'), null) │
├──────────────────────────────────────────────────────────┤
│ NULL                                                     │
└──────────────────────────────────────────────────────────┘

SELECT JSON_PATH_MATCH(NULL, '$.a == 1');

┌───────────────────────────────────┐
│ json_path_match(null, '$.a == 1') │
├───────────────────────────────────┤
│ NULL                              │
└───────────────────────────────────┘
```
