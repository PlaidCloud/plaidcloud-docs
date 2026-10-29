---
title: INSTR（Lakehouse v1）
description: INSTR——返回子串 substr 在字符串 str 中首次出现的位置。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/instr.md
---

返回子串 substr 在字符串 str 中首次出现的位置。
这与 LOCATE() 的双参数形式相同，只是参数顺序相反。

## Analyze 语法

```python
func.instr(<str>, <substr>)
```

## Analyze 示例

```python
func.instr('foobarbar', 'bar')
┌────────────────────────────────┐
│ func.instr('foobarbar', 'bar') │
├────────────────────────────────┤
│                              4 │
└────────────────────────────────┘
```

## SQL 语法

```sql
INSTR(<str>, <substr>)
```

## 参数

| 参数  | 说明           |
|------------|----------------|
| `<str>`    | 字符串。       |
| `<substr>` | 子串。         |

## 返回类型

`BIGINT`

## SQL 示例

```sql
SELECT INSTR('foobarbar', 'bar');
┌───────────────────────────┐
│ INSTR('foobarbar', 'bar') │
├───────────────────────────┤
│                         4 │
└───────────────────────────┘

SELECT INSTR('xbar', 'foobar');
┌─────────────────────────┐
│ INSTR('xbar', 'foobar') │
├─────────────────────────┤
│                       0 │
└─────────────────────────┘
```
