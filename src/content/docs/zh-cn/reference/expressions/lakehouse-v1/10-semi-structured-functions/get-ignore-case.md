---
title: GET_IGNORE_CASE（Lakehouse v1）
description: GET_IGNORE_CASE — 按字段名从包含 OBJECT 的 VARIANT 中提取值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/get-ignore-case.md
---

按 field_name 从包含 `OBJECT` 的 `VARIANT` 中提取值。
返回值为 `Variant`；如果任一参数为 `NULL`，则返回 `NULL`。

`GET_IGNORE_CASE` 与 `GET` 类似，但对字段名应用不区分大小写的匹配。
先匹配完全相同的字段名，找不到时，再按字母顺序匹配不区分大小写的字段名。

## Analyze 语法

```python
func.get_ignore_Case(<variant>, <field_name>)
```

## Analyze 示例

```python
func.get_ignore_case(func.parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA')
┌─────────────────────────────────────────────────────────────────────────┐
│ func.get_ignore_case(func.parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA') │
├─────────────────────────────────────────────────────────────────────────┤
│ 3                                                                       │
└─────────────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
GET_IGNORE_CASE( <variant>, <field_name> )
```

## 参数

| 参数           | 说明                                       |
|----------------|--------------------------------------------|
| `<variant>`    | 包含 ARRAY 或 OBJECT 的 VARIANT 值         |
| `<field_name>` | 字符串值，指定 OBJECT 键值对中的键         |

## 返回类型

VARIANT

## SQL 示例

```sql
SELECT get_ignore_case(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA');
┌───────────────────────────────────────────────────────────────┐
│ get_ignore_case(parse_json('{"aa":1, "aA":2, "Aa":3}'), 'AA') │
├───────────────────────────────────────────────────────────────┤
│ 3                                                             │
└───────────────────────────────────────────────────────────────┘
```
