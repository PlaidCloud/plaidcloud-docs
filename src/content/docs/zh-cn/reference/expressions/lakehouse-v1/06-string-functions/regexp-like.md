---
title: REGEXP_LIKE（Lakehouse v1）
description: REGEXP_LIKE——检查字符串是否匹配正则表达式。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-like.md
---

REGEXP_LIKE 函数用于检查字符串是否匹配正则表达式。

## Analyze 语法

```python
func.regexp_like(<expr>, <pat[, match_type]>)
```

## Analyze 示例

```python
func.regexp_like('a', '^[a-d]')
┌─────────────────────────────────┐
│ func.regexp_like('a', '^[a-d]') │
├─────────────────────────────────┤
│                               1 │
└─────────────────────────────────┘
```

## SQL 语法

```sql
REGEXP_LIKE(<expr>, <pat[, match_type]>)
```

## 参数

| 参数      | 说明                                                                       |
|----------------|-----------------------------------------------------------------------------------|
| `<expr>`       | 待匹配的字符串 expr                                                |
| `<pat>`        | 正则表达式                                                            |
| `[match_type]` | 可选。match_type 参数是指定匹配方式的字符串 |

`match_type` 可以包含以下任意或全部字符：

* `c`：区分大小写匹配。
* `i`：不区分大小写匹配。
* `m`：多行模式。识别字符串内部的行终止符。默认行为是仅在字符串表达式的开头和结尾匹配行终止符。
* `n`：`.` 字符可匹配行终止符。默认情况下，`.` 的匹配在行尾停止。
* `u`：仅 Unix 行尾。目前不受支持。

## 返回类型

`BIGINT`
如果字符串 expr 与模式 pat 指定的正则表达式匹配，则返回 `1`，否则返回 `0`。如果 expr 或 pat 为 NULL，则返回值为 NULL。

## SQL 示例

```sql
SELECT REGEXP_LIKE('a', '^[a-d]');
┌────────────────────────────┐
│ REGEXP_LIKE('a', '^[a-d]') │
├────────────────────────────┤
│                          1 │
└────────────────────────────┘

SELECT REGEXP_LIKE('abc', 'ABC');
┌───────────────────────────┐
│ REGEXP_LIKE('abc', 'ABC') │
├───────────────────────────┤
│                         1 │
└───────────────────────────┘

SELECT REGEXP_LIKE('abc', 'ABC', 'c');
┌────────────────────────────────┐
│ REGEXP_LIKE('abc', 'ABC', 'c') │
├────────────────────────────────┤
│                              0 │
└────────────────────────────────┘

SELECT REGEXP_LIKE('new*\n*line', 'new\\*.\\*line');

┌───────────────────────────────────────────┐
│ REGEXP_LIKE('new*\n*line', 'new\*.\*line')│
├───────────────────────────────────────────┤
│                                         0 │
└───────────────────────────────────────────┘

SELECT REGEXP_LIKE('new*\n*line', 'new\\*.\\*line', 'n');

┌────────────────────────────────────────────────┐
│ REGEXP_LIKE('new*\n*line', 'new\*.\*line', 'n')│
├────────────────────────────────────────────────┤
│                                              1 │
└────────────────────────────────────────────────┘
```
