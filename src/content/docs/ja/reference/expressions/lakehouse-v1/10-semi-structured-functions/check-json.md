---
title: CHECK_JSON (Lakehouse v1)
description: CHECK_JSON — JSONドキュメントが有効かどうかをチェックします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/check-json.md
---

JSONドキュメントが有効かどうかをチェックします。
入力文字列が有効なJSONドキュメントまたは `NULL` の場合、出力は `NULL` になります。
入力を有効なJSON値に変換できない場合、出力文字列にエラーメッセージが含まれます。

## Analyze構文

```python
func.check_json(<expr>)
```

## Analyzeの例

```python
func.check_json('[1,2,3]');
┌────────────────────────────┐
│ func.check_json('[1,2,3]') │
├────────────────────────────┤
│ NULL                       │
└────────────────────────────┘
```

## SQL構文

```sql
CHECK_JSON( <expr> )
```

## 引数

| 引数 | 説明                  |
|-----------|------------------------------|
| `<expr>`  | 文字列型の式 |

## 戻り値の型

文字列

## SQLの例

```sql
SELECT check_json('[1,2,3]');
┌───────────────────────┐
│ check_json('[1,2,3]') │
├───────────────────────┤
│ NULL                  │
└───────────────────────┘

SELECT check_json('{"key":"val"}');
┌─────────────────────────────┐
│ check_json('{"key":"val"}') │
├─────────────────────────────┤
│ NULL                        │
└─────────────────────────────┘

SELECT check_json('{"key":');
┌──────────────────────────────────────────────┐
│ check_json('{"key":')                        │
├──────────────────────────────────────────────┤
│ EOF while parsing a value at line 1 column 7 │
└──────────────────────────────────────────────┘
```
