---
title: "AS_<type> (Lakehouse v1)"
description: AS_<type> — VARIANT値を他のデータ型に厳密にキャストします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/as-type.md
---

`VARIANT` 値を他のデータ型に厳密にキャストします。
入力のデータ型が `VARIANT` でない場合、出力は `NULL` になります。
`VARIANT` 内の値の型が出力する型と一致しない場合も、出力は `NULL` になります。

## Analyze構文
```python
func.as_boolean( <variant> )
func.as_integer( <variant> )
func.as_float( <variant> )
func.as_string( <variant> )
func.as_array( <variant> )
func.as_object( <variant> )
```

## SQL構文

```sql
AS_BOOLEAN( <variant> )
AS_INTEGER( <variant> )
AS_FLOAT( <variant> )
AS_STRING( <variant> )
AS_ARRAY( <variant> )
AS_OBJECT( <variant> )
```

## 引数

| 引数   | 説明       |
|-------------|-------------------|
| `<variant>` | VARIANT値 |

## 戻り値の型

- AS_BOOLEAN: BOOLEAN
- AS_INTEGER: BIGINT
- AS_FLOAT:   DOUBLE
- AS_STRING:  VARCHAR
- AS_ARRAY:   配列を含むVariant
- AS_OBJECT:  オブジェクトを含むVariant

## SQLの例

```sql
SELECT as_boolean(parse_json('true'));
┌────────────────────────────────┐
│ as_boolean(parse_json('true')) │
├────────────────────────────────┤
│ 1                              │
└────────────────────────────────┘

SELECT as_integer(parse_json('123'));
┌───────────────────────────────┐
│ as_integer(parse_json('123')) │
├───────────────────────────────┤
│ 123                           │
└───────────────────────────────┘

SELECT as_float(parse_json('12.34'));
┌───────────────────────────────┐
│ as_float(parse_json('12.34')) │
├───────────────────────────────┤
│ 12.34                         │
└───────────────────────────────┘

SELECT as_string(parse_json('"abc"'));
┌────────────────────────────────┐
│ as_string(parse_json('"abc"')) │
├────────────────────────────────┤
│ abc                            │
└────────────────────────────────┘

SELECT as_array(parse_json('[1,2,3]'));
┌─────────────────────────────────┐
│ as_array(parse_json('[1,2,3]')) │
├─────────────────────────────────┤
│ [1,2,3]                         │
└─────────────────────────────────┘

SELECT as_object(parse_json('{"k":"v","a":"b"}'));
┌────────────────────────────────────────────┐
│ as_object(parse_json('{"k":"v","a":"b"}')) │
├────────────────────────────────────────────┤
│ {"k":"v","a":"b"}                          │
└────────────────────────────────────────────┘

```
