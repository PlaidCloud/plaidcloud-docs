---
title: "GET（半结构化，Lakehouse v1）"
description: GET — 按索引从包含 ARRAY 的 Variant 中提取值，或从 Variant 中提取值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/get.md
---

按 `index` 从包含 `ARRAY` 的 `Variant` 中提取值，或按 `field_name` 从包含 `OBJECT` 的 `Variant` 中提取值。
返回值为 `Variant`；如果任一参数为 `NULL`，则返回 `NULL`。

`GET` 对 `field_name` 应用区分大小写的匹配。如需不区分大小写的匹配，请使用 `GET_IGNORE_CASE`。

## Analyze 语法

```python
func.get(<variant>, <index>)

or

func.get(<variant>, <field_name>)
```

## Analyze 示例

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

## SQL 语法

```sql
GET( <variant>, <index> )

GET( <variant>, <field_name> )
```

## 参数

| 参数           | 说明                                       |
|----------------|--------------------------------------------|
| `<variant>`    | 包含 ARRAY 或 OBJECT 的 VARIANT 值         |
| `<index>`      | Uint32 值，指定值在 ARRAY 中的位置         |
| `<field_name>` | 字符串值，指定 OBJECT 键值对中的键         |

## 返回类型

VARIANT

## SQL 示例

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
