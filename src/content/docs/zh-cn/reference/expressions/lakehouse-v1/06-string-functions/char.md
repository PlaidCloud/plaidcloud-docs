---
title: CHAR（Lakehouse v1）
description: CHAR——返回传入的每个整数对应的字符。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/char.md
---

返回传入的每个整数对应的字符。

## Analyze 语法

```python
func.char(N,...)
```

## Analyze 示例

```python
func.char(77,121,83,81,76)
┌─────────────────────────────┐
│ func.char(77,121,83,81,76) │
├─────────────────────────────┤
│ 4D7953514C                  │
└─────────────────────────────┘
```

## SQL 语法

```sql
CHAR(N, ...)
```

## 参数

| 参数 | 说明    |
|-----------|----------------|
| N         | 数值列         |

## 返回类型

`BINARY`

## SQL 示例

此示例同时显示返回的二进制值及其字符串表示。

```sql
SELECT CHAR(77,121,83,81,76) as a, a::String;
┌────────────────────────┐
│      a     │ a::string │
│   Binary   │   String  │
├────────────┼───────────┤
│ 4D7953514C │ MySQL     │
└────────────────────────┘
```
