---
title: REVERSE（Lakehouse v1）
description: REVERSE——返回字符顺序反转后的字符串 str。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/reverse.md
---

返回字符顺序反转后的字符串 str。

## Analyze 语法

```python
func.reverse(<str>)
```

## Analyze 示例

```python
func.reverse('abc')
┌──────────────────────┐
│ func..reverse('abc') │
├──────────────────────┤
│ cba                  │
└──────────────────────┘
```

## SQL 语法

```sql
REVERSE(<str>)
```

## 参数

| 参数 | 说明       |
|-----------|-------------------|
| `<str>`   | 字符串值。 |

## 返回类型

`VARCHAR`

## SQL 示例

```sql
SELECT REVERSE('abc');
┌────────────────┐
│ REVERSE('abc') │
├────────────────┤
│ cba            │
└────────────────┘
```
