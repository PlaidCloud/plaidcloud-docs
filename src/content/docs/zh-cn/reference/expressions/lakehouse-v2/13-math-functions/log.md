---
title: LOG (Lakehouse v2)
description: LOG — 返回数值以指定底数为底的对数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/log.md
---

返回数值以指定底数为底的对数。

## Analyze 语法

```python
func.log(<base>, <x>)
```

## Analyze 示例

```python
func.log(10, 100)

┌─────┐
│ 2.0  │
└─────┘
```

## SQL 语法

```sql
LOG(<base>, <x>)
```

## SQL 示例

```sql
SELECT LOG(10, 100);

┌─────┐
│ 2.0  │
└─────┘
```
