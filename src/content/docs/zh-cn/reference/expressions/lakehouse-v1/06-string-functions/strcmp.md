---
title: STRCMP（Lakehouse v1）
description: STRCMP——字符串相同时返回 0，第一个参数小于第二个参数时返回 -1，否则返回 1。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/strcmp.md
---

字符串相同时返回 0，第一个参数小于第二个参数时返回 -1，否则返回 1。

## Analyze 语法

```python
func.strcmp(<expr1> ,<expr2>)
```

## Analyze 示例

```python
func.strcmp('text', 'text2')
┌──────────────────────────────┐
│ func.strcmp('text', 'text2') │
├──────────────────────────────┤
│                           -1 │
└──────────────────────────────┘

func.strcmp('text2', 'text')
┌──────────────────────────────┐
│ func.strcmp('text2', 'text') │
├──────────────────────────────┤
│                            1 │
└──────────────────────────────┘

func.strcmp('text', 'text')
┌──────────────────────────────┐
│ func.strcmp('text', 'text')  │
├──────────────────────────────┤
│                            0 │
└──────────────────────────────┘
```

## SQL 语法

```sql
STRCMP(<expr1> ,<expr2>)
```

## 参数

| 参数 | 说明 |
|-----------|-------------|
| `<expr1>` | 字符串。 |
| `<expr2>` | 字符串。 |

## 返回类型

`BIGINT`

## SQL 示例

```sql
SELECT STRCMP('text', 'text2');
┌─────────────────────────┐
│ STRCMP('text', 'text2') │
├─────────────────────────┤
│                      -1 │
└─────────────────────────┘

SELECT STRCMP('text2', 'text');
┌─────────────────────────┐
│ STRCMP('text2', 'text') │
├─────────────────────────┤
│                       1 │
└─────────────────────────┘

SELECT STRCMP('text', 'text');
┌────────────────────────┐
│ STRCMP('text', 'text') │
├────────────────────────┤
│                      0 │
└────────────────────────┘
```
