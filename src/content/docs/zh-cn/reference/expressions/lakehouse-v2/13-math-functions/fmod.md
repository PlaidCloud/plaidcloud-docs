---
title: FMOD (Lakehouse v2)
description: FMOD — 返回两个数相除的浮点余数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/fmod.md
---

返回两个数相除的浮点余数。

## Analyze 语法

```python
func.fmod(<x>, <y>)
```

## Analyze 示例

```python
func.fmod(10.5, 3.0)

┌─────┐
│ 1.5  │
└─────┘
```

## SQL 语法

```sql
FMOD(<x>, <y>)
```

## SQL 示例

```sql
SELECT FMOD(10.5, 3.0);

┌─────┐
│ 1.5  │
└─────┘
```
