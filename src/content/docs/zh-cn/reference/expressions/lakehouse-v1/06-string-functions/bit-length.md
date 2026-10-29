---
title: BIT_LENGTH（Lakehouse v1）
description: BIT_LENGTH——返回字符串的位长度。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/bit-length.md
---

返回字符串的位长度。

## Analyze 语法

```python
func.bit_length(<expr>)
```

## Analyze 示例

```python
func.bit_length('Word')
┌─────────────────────────┐
│ func.bit_length('Word') │
├─────────────────────────┤
│                      32 │
└─────────────────────────┘
```

## SQL 语法

```sql
BIT_LENGTH(<expr>)
```

## 参数

| 参数 | 说明 |
|-----------| ----------- |
| `<expr>`  | 字符串。 |

## 返回类型

`BIGINT`

## SQL 示例

```sql
SELECT BIT_LENGTH('Word');
┌────────────────────────────┐
│ SELECT BIT_LENGTH('Word'); │
├────────────────────────────┤
│ 32                         │
└────────────────────────────┘
```
