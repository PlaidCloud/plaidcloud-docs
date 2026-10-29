---
title: CONCAT（Lakehouse v1）
description: CONCAT——返回连接各参数后得到的字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/concat.md
---

返回连接各参数后得到的字符串。可以有一个或多个参数。如果所有参数都是非二进制字符串，则结果为非二进制字符串；如果参数中包含任何二进制字符串，则结果为二进制字符串。数值参数会被转换为等效的非二进制字符串形式。

## Analyze 语法

```python
func.concat(<expr1>, ...)
```

## Analyze 示例

```python
func.concat('data', 'bend')
┌─────────────────────────────┐
│ func.concat('data', 'bend') │
├─────────────────────────────┤
│ databend                    │
└─────────────────────────────┘
```

## SQL 语法

```sql
CONCAT(<expr1>, ...)
```

## 参数

| 参数 | 说明 |
|-----------|-------------|
| `<expr1>` | 字符串      |

## 返回类型

`VARCHAR` 数据类型的值或 `NULL`。

## SQL 示例

```sql
SELECT CONCAT('data', 'bend');
┌────────────────────────┐
│ concat('data', 'bend') │
├────────────────────────┤
│ databend               │
└────────────────────────┘

SELECT CONCAT('data', NULL, 'bend');
┌──────────────────────────────┐
│ CONCAT('data', NULL, 'bend') │
├──────────────────────────────┤
│                         NULL │
└──────────────────────────────┘

SELECT CONCAT('14.3');
┌────────────────┐
│ concat('14.3') │
├────────────────┤
│ 14.3           │
└────────────────┘
```
