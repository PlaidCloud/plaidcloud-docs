---
title: SUBSTR（Lakehouse v1）
description: SUBSTR——从指定位置开始提取包含特定数量字符的字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/substr.md
---

从给定字符串的指定位置开始提取包含特定数量字符的字符串。

- 不带 `len` 参数的形式返回字符串 `str` 中从位置 `pos` 开始的子串。
- 带 `len` 参数的形式返回字符串 `str` 中从位置 `pos` 开始、长度为 `len` 个字符的子串。

`pos` 也可以使用负值。此时，子串的起点是从字符串末尾而不是开头算起的第 pos 个字符。该函数的任何形式都可以对 `pos` 使用负值。`pos` 为 0 时返回空字符串。待提取子串的字符串中，第一个字符的位置计为 1。

## Analyze 语法

```python
func.substr(<str>, <pos>, <len>)
```

## Analyze 示例

```python
func.substr('Quadratically', 5, 6)
┌────────────────────────────────────┐
│ func.substr('Quadratically', 5, 6) │
├────────────────────────────────────┤
│ ratica                             │
└────────────────────────────────────┘
```

## SQL 语法

```sql
SUBSTR(<str>, <pos>)

SUBSTR(<str>, <pos>, <len>)
```

## 参数

| 参数 | 说明                                                                                |
|-----------|--------------------------------------------------------------------------------------------|
| `<str>`   | 要从中提取字符的主字符串                                   |
| `<pos>`   | 子串的起始位置（从 1 开始）。为负数时从末尾开始计数 |
| `<len>`   | 要提取的子串的最大长度                                             |

## 别名

- [SUBSTRING](../substring)
- [MID](../mid)

## 返回类型

VARCHAR

## SQL 示例

```sql
SELECT
  SUBSTRING('Quadratically', 5),
  SUBSTR('Quadratically', 5),
  MID('Quadratically', 5);

┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│ substring('quadratically' from 5) │ substring('quadratically' from 5) │ mid('quadratically', 5) │
├───────────────────────────────────┼───────────────────────────────────┼─────────────────────────┤
│ ratically                         │ ratically                         │ ratically               │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘

SELECT
  SUBSTRING('Quadratically', 5, 6),
  SUBSTR('Quadratically', 5, 6),
  MID('Quadratically', 5, 6);

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ substring('quadratically' from 5 for 6) │ substring('quadratically' from 5 for 6) │ mid('quadratically', 5, 6) │
├─────────────────────────────────────────┼─────────────────────────────────────────┼────────────────────────────┤
│ ratica                                  │ ratica                                  │ ratica                     │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
