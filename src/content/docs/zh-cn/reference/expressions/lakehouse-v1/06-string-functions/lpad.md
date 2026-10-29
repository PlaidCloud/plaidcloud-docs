---
title: LPAD（Lakehouse v1）
description: LPAD——返回字符串 str，在左侧用字符串 padstr 填充至 len 个字符的长度。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/lpad.md
---

返回字符串 str，在左侧用字符串 padstr 填充至 len 个字符的长度。
如果 str 比 len 长，则返回值会被截短为 len 个字符。

## Analyze 语法

```python
func.lpad(<str>, <len>, <padstr>)
```

## Analyze 示例

```python
func.lpad('hi',4,'??')
┌────────────────────────┐
│ func.lpad('hi',4,'??') │
├────────────────────────┤
│ ??hi                   │
└────────────────────────┘
```

```python
func.lpad('hi',1,'??')
┌────────────────────────┐
│ func.lpad('hi',1,'??') │
├────────────────────────┤
│ h                      │
└────────────────────────┘
```

## SQL 语法

```sql
LPAD(<str>, <len>, <padstr>)
```

## 参数

| 参数  | 说明             |
|------------|-----------------|
| `<str>`    | 字符串。         |
| `<len>`    | 长度。           |
| `<padstr>` | 填充字符串。     |

## 返回类型

`VARCHAR`

## SQL 示例

```sql
SELECT LPAD('hi',4,'??');
┌─────────────────────┐
│ LPAD('hi', 4, '??') │
├─────────────────────┤
│ ??hi                │
└─────────────────────┘

SELECT LPAD('hi',1,'??');
┌─────────────────────┐
│ LPAD('hi', 1, '??') │
├─────────────────────┤
│ h                   │
└─────────────────────┘
```
