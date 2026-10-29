---
title: GET_IGNORE_CASE (Lakehouse v1)
description: GET_IGNORE_CASE — OBJECTを含むVARIANTから、field_nameを指定して値を抽出します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/get-ignore-case.md
---

`OBJECT` を含む `VARIANT` から、field_nameを指定して値を抽出します。
値は `Variant` として返されます。いずれかの引数が `NULL` の場合は `NULL` を返します。

`GET_IGNORE_CASE` は `GET` と似ていますが、フィールド名の照合で大文字と小文字を区別しません。
まずフィールド名が完全に同じものを照合し、見つからない場合は、大文字と小文字を区別せずにアルファベット順で照合します（最初の一致を返します）。

## Analyze構文

```python
func.get_ignore_Case(<variant>, <field_name>)
```

## Analyzeの例

```python
func.get_ignore_case(func.parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA')
┌─────────────────────────────────────────────────────────────────────────┐
│ func.get_ignore_case(func.parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA') │
├─────────────────────────────────────────────────────────────────────────┤
│ 3                                                                       │
└─────────────────────────────────────────────────────────────────────────┘
```

## SQL構文

```sql
GET_IGNORE_CASE( <variant>, <field_name> )
```

## 引数

| 引数      | 説明                                                      |
|----------------|------------------------------------------------------------------|
| `<variant>`    | ARRAYまたはOBJECTを含むVARIANT値     |
| `<field_name>` | OBJECTのキーと値のペアにおけるキーを指定する文字列値 |

## 戻り値の型

VARIANT

## SQLの例

```sql
SELECT get_ignore_case(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA');
┌───────────────────────────────────────────────────────────────┐
│ get_ignore_case(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA') │
├───────────────────────────────────────────────────────────────┤
│ 3                                                             │
└───────────────────────────────────────────────────────────────┘
```
