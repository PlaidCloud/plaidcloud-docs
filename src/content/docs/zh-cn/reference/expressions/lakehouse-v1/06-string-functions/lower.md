---
title: LOWER（Lakehouse v1）
description: LOWER——返回所有字符均转换为小写的字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/lower.md
---

返回所有字符均转换为小写的字符串。

## Analyze 语法

```python
func.lower(<str>)
```

## Analyze 示例

```python
func.lower('Hello, PlaidCloud!')
┌──────────────────────────────────┐
│ func.lower('Hello, PlaidCloud!') │
├──────────────────────────────────┤
│ hello, plaidcloud!               │
└──────────────────────────────────┘
```

## SQL 语法

```sql
LOWER(<str>)
```

## 别名

- [LCASE](../lcase)

## 返回类型

VARCHAR

## SQL 示例

```sql
SELECT LOWER('Hello, Databend!'), LCASE('Hello, Databend!');

┌───────────────────────────────────────────────────────┐
│ lower('hello, databend!') │ lcase('hello, databend!') │
├───────────────────────────┼───────────────────────────┤
│ hello, databend!          │ hello, databend!          │
└───────────────────────────────────────────────────────┘
```
