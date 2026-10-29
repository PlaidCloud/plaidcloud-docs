---
title: LEFT（Lakehouse v1）
description: LEFT——返回字符串 str 最左侧的 len 个字符；任何参数为 NULL 时返回 NULL。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/left.md
---

返回字符串 str 最左侧的 len 个字符；任何参数为 NULL 时返回 NULL。

## Analyze 语法

```python
func.left(<str>, <len>)
```

## Analyze 示例

```python
func.left('foobarbar', 5)
┌───────────────────────────┐
│ func.left('foobarbar', 5) │
├───────────────────────────┤
│ fooba                     │
└───────────────────────────┘
```

## SQL 语法

```sql
LEFT(<str>, <len>);
```

## 参数

| 参数 | 说明                     |
|-----------|----------------------------------------------------------|
| `<str>`   | 要从中提取字符的主字符串 |
| `<len>`   | 字符数                   |

## 返回类型

`VARCHAR`

## SQL 示例

```sql
SELECT LEFT('foobarbar', 5);
┌──────────────────────┐
│ LEFT('foobarbar', 5) │
├──────────────────────┤
│ fooba                │
└──────────────────────┘
```
