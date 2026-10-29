---
title: RIGHT（Lakehouse v1）
description: RIGHT——返回字符串 str 最右侧的 len 个字符；任何参数为 NULL 时返回 NULL。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/right.md
---

返回字符串 str 最右侧的 len 个字符；任何参数为 NULL 时返回 NULL。

## Analyze 语法

```python
func.right(<str>, <len>)
```

## Analyze 示例

```python
func.right('foobarbar', 4)
┌────────────────────────────┐
│ func.right('foobarbar', 4) │
├────────────────────────────┤
│ rbar                       │
└────────────────────────────┘
```

## SQL 语法

```sql
RIGHT(<str>, <len>);
```

## 参数

| 参数 | 说明                                              |
|-----------|----------------------------------------------------------|
| `<str>`   | 要从中提取字符的主字符串 |
| `<len>`   | 字符数                                  |

## 返回类型

`VARCHAR`

## SQL 示例

```sql
SELECT RIGHT('foobarbar', 4);
┌───────────────────────┐
│ RIGHT('foobarbar', 4) │
├───────────────────────┤
│ rbar                  │
└───────────────────────┘
```
