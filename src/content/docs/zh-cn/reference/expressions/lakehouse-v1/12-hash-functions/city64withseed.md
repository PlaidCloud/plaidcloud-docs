---
title: CITY64WITHSEED (Lakehouse v1)
description: CITY64WITHSEED：计算字符串的 City64WithSeed 64 位哈希值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/city64withseed.md
---

计算字符串的 City64WithSeed 64 位哈希值。

## Analyze 语法

```python
func.city64withseed(<expr1>, <expr2>)
```

## Analyze 示例

```python
func.city64withseed('1234567890', 12)

┌───────────────────────────────────────┐
│ func.city64withseed('1234567890', 12) │
├───────────────────────────────────────┤
│                  10660895976650300430 │
└───────────────────────────────────────┘
```

## SQL 语法

```sql
CITY64WITHSEED(<expr1>, <expr2>)
```

## SQL 示例

```sql
SELECT CITY64WITHSEED('1234567890', 12);

┌──────────────────────────────────┐
│ city64withseed('1234567890', 12) │
├──────────────────────────────────┤
│             10660895976650300430 │
└──────────────────────────────────┘
```
