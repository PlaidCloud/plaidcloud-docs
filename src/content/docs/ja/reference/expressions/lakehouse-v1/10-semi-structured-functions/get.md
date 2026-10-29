---
title: "GET (Semi-Structured, Lakehouse v1)"
description: GET — ARRAYを含むVariantからインデックスを指定して、またはOBJECTを含むVariantからフィールド名を指定して値を抽出します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/get.md
---

`ARRAY` を含む `Variant` から `index` を指定して、または `OBJECT` を含む `Variant` から `field_name` を指定して値を抽出します。
値は `Variant` として返されます。いずれかの引数が `NULL` の場合は `NULL` を返します。

`GET` は `field_name` の照合で大文字と小文字を区別します。大文字と小文字を区別せずに照合するには、`GET_IGNORE_CASE` を使用します。

## Analyze構文

```python
func.get(<variant>, <index>)

or

func.get(<variant>, <field_name>)
```

## Analyzeの例

```python
func.get(func.parse_json('[2.71, 3.14]'), 0);
┌──────────────────────────────────────────────┐
│ func.get(func.parse_json('[2.71, 3.14]'), 0) │
├──────────────────────────────────────────────┤
│ 2.71                                         │
└──────────────────────────────────────────────┘


func.get(func.parse_json('{"aa":1, "aA":2, "Aa":3}'), 'aa');
┌─────────────────────────────────────────────────────────────┐
│ func.get(func.parse_json('{"aa":1, "aA":2, "Aa":3}'), 'aa') │
├─────────────────────────────────────────────────────────────┤
│ 1                                                           │
└─────────────────────────────────────────────────────────────┘
```

## SQL構文

```sql
GET( <variant>, <index> )

GET( <variant>, <field_name> )
```

## 引数

| 引数      | 説明                                                      |
|----------------|------------------------------------------------------------------|
| `<variant>`    | ARRAYまたはOBJECTを含むVARIANT値     |
| `<index>`      | ARRAY内の値の位置を指定するUint32値    |
| `<field_name>` | OBJECTのキーと値のペアにおけるキーを指定する文字列値 |

## 戻り値の型

VARIANT

## SQLの例

```sql
SELECT get(parse_json('[2.71, 3.14]'), 0);
┌────────────────────────────────────┐
│ get(parse_json('[2.71, 3.14]'), 0) │
├────────────────────────────────────┤
│ 2.71                               │
└────────────────────────────────────┘

SELECT get(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'aa');
┌───────────────────────────────────────────────────┐
│ get(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'aa') │
├───────────────────────────────────────────────────┤
│ 1                                                 │
└───────────────────────────────────────────────────┘

SELECT get(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA');
┌───────────────────────────────────────────────────┐
│ get(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA') │
├───────────────────────────────────────────────────┤
│ NULL                                              │
└───────────────────────────────────────────────────┘
```
