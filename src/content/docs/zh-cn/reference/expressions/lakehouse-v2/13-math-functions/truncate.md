---
title: TRUNCATE (Lakehouse v2)
description: TRUNCATE — 将数值截断到指定的小数位数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/truncate.md
---

将数值截断到指定的小数位数。

## Analyze 语法

```python
func.truncate(<x>, <d>)
```

## Analyze 示例

```python
func.truncate(3.14159, 2)

┌──────┐
│ 3.14  │
└──────┘
```

## SQL 语法

```sql
TRUNCATE(<x>, <d>)
```

## SQL 示例

```sql
SELECT TRUNCATE(3.14159, 2);

┌──────┐
│ 3.14  │
└──────┘
```
