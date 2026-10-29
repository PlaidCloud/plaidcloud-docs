---
title: UPPER (Lakehouse v1)
description: UPPER：返回所有字符均转换为大写的字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/upper.md
---

返回所有字符均转换为大写的字符串。

## Analyze 语法

```python
func.unhex(<expr>)
```

## Analyze 示例

```python
func.upper('hello, plaidcloud lakehouse!')
┌────────────────────────────────────────────┐
│ func.upper('hello, plaidcloud lakehouse!') │
├────────────────────────────────────────────┤
│ 'HELLO, PLAIDCLOUD LAKEHOUSE!'             │
└────────────────────────────────────────────┘
```

## SQL 语法

```sql
UPPER(<str>)
```

## 别名

- [UCASE](../ucase)

## 返回类型

VARCHAR

## SQL 示例

```sql
SELECT UPPER('hello, databend!'), UCASE('hello, databend!');

┌───────────────────────────────────────────────────────┐
│ upper('hello, databend!') │ ucase('hello, databend!') │
├───────────────────────────┼───────────────────────────┤
│ HELLO, DATABEND!          │ HELLO, DATABEND!          │
└───────────────────────────────────────────────────────┘
```
