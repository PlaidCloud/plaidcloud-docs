---
title: LOCATE（Lakehouse v1）
description: LOCATE——第一种语法返回子串 substr 在字符串 str 中首次出现的位置。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/locate.md
---

第一种语法返回子串 substr 在字符串 str 中首次出现的位置。
第二种语法返回子串 substr 在字符串 str 中从位置 pos 开始首次出现的位置。
如果 str 中不包含 substr，则返回 0。任何参数为 NULL 时返回 NULL。

## Analyze 语法

```python
func.locate(<substr>, <str>, <pos>)
```

## Analyze 示例

```python
func.locate('bar', 'foobarbar')
┌────────────────────────────────────┐
│ func.locate('bar', 'foobarbar') │
├────────────────────────────────────┤
│                                  5 │
└────────────────────────────────────┘
```

```python
func.locate('bar', 'foobarbar', 5)
┌────────────────────────────────────┐
│ func.locate('bar', 'foobarbar', 5) │
├────────────────────────────────────┤
│                                  7 │
└────────────────────────────────────┘
```

## SQL 语法

```sql
LOCATE(<substr>, <str>)
LOCATE(<substr>, <str>, <pos>)
```

## 参数

| 参数  | 说明           |
|------------|----------------|
| `<substr>` | 子串。         |
| `<str>`    | 字符串。       |
| `<pos>`    | 位置。         |

## 返回类型

`BIGINT`

## SQL 示例

```sql
SELECT LOCATE('bar', 'foobarbar')
┌────────────────────────────┐
│ LOCATE('bar', 'foobarbar') │
├────────────────────────────┤
│                          4 │
└────────────────────────────┘

SELECT LOCATE('xbar', 'foobar')
┌──────────────────────────┐
│ LOCATE('xbar', 'foobar') │
├──────────────────────────┤
│                        0 │
└──────────────────────────┘

SELECT LOCATE('bar', 'foobarbar', 5)
┌───────────────────────────────┐
│ LOCATE('bar', 'foobarbar', 5) │
├───────────────────────────────┤
│                             7 │
└───────────────────────────────┘
```
