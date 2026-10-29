---
title: POSITION（Lakehouse v1）
description: POSITION——POSITION(substr IN str) 是 LOCATE(substr,str) 的同义词。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/position.md
---

POSITION(substr IN str) 是 LOCATE(substr,str) 的同义词。
返回子串 substr 在字符串 str 中首次出现的位置。
如果 str 中不包含 substr，则返回 0。任何参数为 NULL 时返回 NULL。

## Analyze 语法

```python
func.position(<substr>, <str>)
```

## Analyze 示例

```python
func.position('bar', 'foobarbar')
┌───────────────────────────────────┐
│ func.position('bar', 'foobarbar') │
├───────────────────────────────────┤
│                                 4 │
└───────────────────────────────────┘
```

## SQL 语法

```sql
POSITION(<substr> IN <str>)
```

## 参数

| 参数  | 说明           |
|------------|----------------|
| `<substr>` | 子串。         |
| `<str>`    | 字符串。       |

## 返回类型

`BIGINT`

## SQL 示例

```sql
SELECT POSITION('bar' IN 'foobarbar')
┌────────────────────────────┐
│ POSITION('bar' IN 'foobarbar') │
├────────────────────────────┤
│                          4 │
└────────────────────────────┘

SELECT POSITION('xbar' IN 'foobar')
┌──────────────────────────┐
│ POSITION('xbar' IN 'foobar') │
├──────────────────────────┤
│                        0 │
└──────────────────────────┘
```
