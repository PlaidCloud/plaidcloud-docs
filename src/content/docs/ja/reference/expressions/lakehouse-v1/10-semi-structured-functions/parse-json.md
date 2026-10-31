---
title: PARSE_JSON (Lakehouse v1)
description: 入力のJSON文字列を解釈し、VARIANT値を生成します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/parse-json.md
---

`parse_json` と `try_parse_json` は、入力文字列をJSONドキュメントとして解釈し、VARIANT値を生成します。

`try_parse_json` は、解析中にエラーが発生した場合にNULL値を返します。

## Analyze構文

```python
func.parse_json(<json_string>)

or

func.try_parse_json(<json_string>)
```

## Analyzeの例

```python
func.parse_json('[-1, 12, 289, 2188, false]')

┌───────────────────────────────────────────────┐
│ func.parse_json('[-1, 12, 289, 2188, false]') │
├───────────────────────────────────────────────┤
│ [-1,12,289,2188,false]                        │
└───────────────────────────────────────────────┘

func.try_parse_json('{ "x" : "abc", "y" : false, "z": 10} ')

┌──────────────────────────────────────────────────────────────┐
│ func.try_parse_json('{ "x" : "abc", "y" : false, "z": 10} ') │
├──────────────────────────────────────────────────────────────┤
│ {"x":"abc","y":false,"z":10}                                 │
└──────────────────────────────────────────────────────────────┘
```

## SQL構文

```sql
PARSE_JSON(<expr>)
TRY_PARSE_JSON(<expr>)
```

## 引数

| 引数 | 説明                                                                    |
|-----------|--------------------------------------------------------------------------------|
| `<expr>`  | 有効なJSON情報を保持する、文字列型（VARCHARなど）の式です。 |

## 戻り値の型

VARIANT

## SQLの例

```sql
SELECT parse_json('[-1, 12, 289, 2188, false]');
┌──────────────────────────────────────────┐
│ parse_json('[-1, 12, 289, 2188, false]') │
├──────────────────────────────────────────┤
│ [-1,12,289,2188,false]                   │
└──────────────────────────────────────────┘

SELECT try_parse_json('{ "x" : "abc", "y" : false, "z": 10} ');
┌─────────────────────────────────────────────────────────┐
│ try_parse_json('{ "x" : "abc", "y" : false, "z": 10} ') │
├─────────────────────────────────────────────────────────┤
│ {"x":"abc","y":false,"z":10}                            │
└─────────────────────────────────────────────────────────┘
```
