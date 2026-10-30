---
title: CONCAT_WS（Lakehouse v1）
description: CONCAT_WS——CONCAT_WS() 表示使用分隔符连接（Concatenate With Separator），是 CONCAT() 的特殊形式。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/concat-ws.md
---

CONCAT_WS() 表示使用分隔符连接（Concatenate With Separator），是 CONCAT() 的特殊形式。第一个参数是其余参数的分隔符，分隔符会添加到待连接的字符串之间。分隔符可以是字符串，其余参数也可以是字符串。如果分隔符为 NULL，则结果为 NULL。

CONCAT_WS() 不会跳过空字符串，但会跳过分隔符参数之后的所有 NULL 值。

## Analyze 语法

```python
func.concat_ws(<separator>, <expr1>, ...)
```

## Analyze 示例

```python
func.concat_ws(',', 'data', 'fuse', 'labs', '2021')
┌─────────────────────────────────────────────────────┐
│ func.concat_ws(',', 'data', 'fuse', 'labs', '2021') │
├─────────────────────────────────────────────────────┤
│ data,fuse,labs,2021                                 │
└─────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
CONCAT_WS(<separator>, <expr1>, ...)
```

## 参数

| 参数     | 说明   |
|---------------| ------------- |
| `<separator>` | 字符串列 |
| `<expr1>`     | 值列  |

## 返回类型

`VARCHAR` 数据类型的值或 `NULL`。

## SQL 示例

```sql
SELECT CONCAT_WS(',', 'data', 'fuse', 'labs', '2021');
┌────────────────────────────────────────────────┐
│ CONCAT_WS(',', 'data', 'fuse', 'labs', '2021') │
├────────────────────────────────────────────────┤
│ data,fuse,labs,2021                            │
└────────────────────────────────────────────────┘

SELECT CONCAT_WS(',', 'data', NULL, 'bend');
┌──────────────────────────────────────┐
│ CONCAT_WS(',', 'data', NULL, 'bend') │
├──────────────────────────────────────┤
│ data,bend                            │
└──────────────────────────────────────┘


SELECT CONCAT_WS(',', 'data', NULL, NULL, 'bend');
┌────────────────────────────────────────────┐
│ CONCAT_WS(',', 'data', NULL, NULL, 'bend') │
├────────────────────────────────────────────┤
│ data,bend                                  │
└────────────────────────────────────────────┘


SELECT CONCAT_WS(NULL, 'data', 'fuse', 'labs');
┌─────────────────────────────────────────┐
│ CONCAT_WS(NULL, 'data', 'fuse', 'labs') │
├─────────────────────────────────────────┤
│                                    NULL │
└─────────────────────────────────────────┘

SELECT CONCAT_WS(',', NULL);
┌──────────────────────┐
│ CONCAT_WS(',', NULL) │
├──────────────────────┤
│                      │
└──────────────────────┘
```
