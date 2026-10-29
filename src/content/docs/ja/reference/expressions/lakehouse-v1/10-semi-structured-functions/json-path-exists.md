---
title: JSON_PATH_EXISTS (Lakehouse v1)
description: JSON_PATH_EXISTS — 指定したパスがJSONデータに存在するかどうかをチェックします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-path-exists.md
---

指定したパスがJSONデータに存在するかどうかをチェックします。

## Analyze構文

```python
func.json_path_exists(<json_data>, <json_path_expression)
```

## Analyzeの例

```python
func.json_path_exists(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ == 1)'), func.json_path_exists(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ > 1)')
┌─────────────────────────────┐
│       Item 1   │  Item 2    │
├────────────────┼────────────┤
│       True     │  False     │
└─────────────────────────────┘
```

## SQL構文

```sql
JSON_PATH_EXISTS(<json_data>, <json_path_expression>)
```

- json_data: 検索対象のJSONデータを指定します。JSONオブジェクトまたは配列を指定できます。

- json_path_expression: JSONデータ内でチェックするパスを、`$` で表されるJSONデータのルートを起点として指定します。式の中に条件を含めることもでき、`@` で評価中の現在のノードまたは要素を参照して、結果を絞り込めます。

## 戻り値の型

この関数は次の値を返します。

- 指定したJSONパス（および条件がある場合はその条件）がJSONデータ内に存在する場合は `true`
- 指定したJSONパス（および条件がある場合はその条件）がJSONデータ内に存在しない場合は `false`
- json_dataまたはjson_path_expressionのいずれかがNULLまたは無効な場合は NULL

## SQLの例

```sql
SELECT JSON_PATH_EXISTS(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ == 1)');

----
true


SELECT JSON_PATH_EXISTS(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ > 1)');

----
false

SELECT JSON_PATH_EXISTS(NULL, '$.a');

----
NULL

SELECT JSON_PATH_EXISTS(parse_json('{"a": 1, "b": 2}'), NULL);

----
NULL
```
