---
title: REGEXP_INSTR（Lakehouse v1）
description: REGEXP_INSTR——返回字符串 expr 中与模式 pat 指定的正则表达式匹配的子串的起始索引，无匹配时返回 0。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-instr.md
---

返回字符串 `expr` 中与模式 `pat` 指定的正则表达式匹配的子串的起始索引，无匹配时返回 `0`。如果 `expr` 或 `pat` 为 NULL，则返回值为 NULL。字符索引从 `1` 开始。

## Analyze 语法

```python
func.regexp_instr(<expr>, <pat[, pos[, occurrence[, return_option[, match_type]]]]>)
```

## Analyze 示例

```python
func.regexp_instr('dog cat dog', 'dog')
┌─────────────────────────────────────────┐
│ func.regexp_instr('dog cat dog', 'dog') │
├─────────────────────────────────────────┤
│                                       1 │
└─────────────────────────────────────────┘
```

## SQL 语法

```sql
REGEXP_INSTR(<expr>, <pat[, pos[, occurrence[, return_option[, match_type]]]]>)
```

## 参数

| 参数     | 说明                                                                                                                                                                                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| expr          | 待匹配的字符串 expr                                                                                                                                                                                                                                     |
| pat           | 正则表达式                                                                                                                                                                                                                                                 |
| pos           | 可选。expr 中开始搜索的位置。省略时默认为 1。                                                                                                                                                                             |
| occurrence    | 可选。要搜索第几次匹配。省略时默认为 1。                                                                                                                                                                                     |
| return_option | 可选。要返回的位置类型。如果该值为 0，REGEXP_INSTR() 返回匹配子串第一个字符的位置；如果为 1，则返回匹配子串之后的位置。省略时默认为 0。 |
| match_type    | 可选。指定匹配方式的字符串，含义与 REGEXP_LIKE() 中的说明相同。                                                                                                                                                              |

## 返回类型

数值数据类型的值。

## SQL 示例

```sql
SELECT REGEXP_INSTR('dog cat dog', 'dog');
┌────────────────────────────────────┐
│ REGEXP_INSTR('dog cat dog', 'dog') │
├────────────────────────────────────┤
│                                  1 │
└────────────────────────────────────┘

SELECT REGEXP_INSTR('dog cat dog', 'dog', 2);
┌───────────────────────────────────────┐
│ REGEXP_INSTR('dog cat dog', 'dog', 2) │
├───────────────────────────────────────┤
│                                     9 │
└───────────────────────────────────────┘

SELECT REGEXP_INSTR('aa aaa aaaa', 'a{2}');
┌─────────────────────────────────────┐
│ REGEXP_INSTR('aa aaa aaaa', 'a{2}') │
├─────────────────────────────────────┤
│                                   1 │
└─────────────────────────────────────┘

SELECT REGEXP_INSTR('aa aaa aaaa', 'a{4}');
┌─────────────────────────────────────┐
│ REGEXP_INSTR('aa aaa aaaa', 'a{4}') │
├─────────────────────────────────────┤
│                                   8 │
└─────────────────────────────────────┘
```
