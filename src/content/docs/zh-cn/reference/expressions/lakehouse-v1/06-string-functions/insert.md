---
title: INSERT（Lakehouse v1）
description: INSERT——返回字符串 str，其中从位置 pos 开始、长度为 len 个字符的子串被替换为字符串 newstr。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/insert.md
---

返回字符串 str，其中从位置 pos 开始、长度为 len 个字符的子串被替换为字符串 newstr。如果 pos 不在字符串长度范围内，则返回原字符串。如果 len 超出从 pos 起剩余字符串的长度，则替换从位置 pos 起的其余全部内容。任何参数为 NULL 时返回 NULL。

## Analyze 语法

```python
func.insert(<str>, <pos>, <len>, <newstr>)
```

## Analyze 示例

```python
func.insert('Quadratic', 3, 4, 'What')
┌────────────────────────────────────────┐
│ func.insert('Quadratic', 3, 4, 'What') │
├────────────────────────────────────────┤
│ QuWhattic                              │
└────────────────────────────────────────┘
```

## SQL 语法

```sql
INSERT(<str>, <pos>, <len>, <newstr>)
```

## 参数

| 参数  | 说明             |
|------------|-----------------|
| `<str>`    | 字符串。         |
| `<pos>`    | 位置。           |
| `<len>`    | 长度。           |
| `<newstr>` | 新字符串。       |

## 返回类型

`VARCHAR`

## SQL 示例

```sql
SELECT INSERT('Quadratic', 3, 4, 'What');
┌───────────────────────────────────┐
│ INSERT('Quadratic', 3, 4, 'What') │
├───────────────────────────────────┤
│ QuWhattic                         │
└───────────────────────────────────┘

SELECT INSERT('Quadratic', -1, 4, 'What');
┌───────────────────────────────────────┐
│ INSERT('Quadratic', (- 1), 4, 'What') │
├───────────────────────────────────────┤
│ Quadratic                             │
└───────────────────────────────────────┘

SELECT INSERT('Quadratic', 3, 100, 'What');
┌─────────────────────────────────────┐
│ INSERT('Quadratic', 3, 100, 'What') │
├─────────────────────────────────────┤
│ QuWhat                              │
└─────────────────────────────────────┘

┌────────────────────────────────────────────┬────────┐
│ INSERT('123456789', number, number, 'aaa') │ number │
├────────────────────────────────────────────┼────────┤
│ 123456789                                  │      0 │
│ aaa23456789                                │      1 │
│ 1aaa456789                                 │      2 │
│ 12aaa6789                                  │      3 │
│ 123aaa89                                   │      4 │
│ 1234aaa                                    │      5 │
│ 12345aaa                                   │      6 │
│ 123456aaa                                  │      7 │
│ 1234567aaa                                 │      8 │
│ 12345678aaa                                │      9 │
│ 123456789                                  │     10 │
│ 123456789                                  │     11 │
│ 123456789                                  │     12 │
└────────────────────────────────────────────┴────────┘
```
