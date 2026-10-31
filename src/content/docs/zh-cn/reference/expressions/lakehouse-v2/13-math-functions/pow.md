---
title: POW (Lakehouse v2)
description: POW — 返回一个数的指定次幂。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/pow.md
---

返回一个数的指定次幂。

## Analyze 语法

```python
func.pow(<x>, <y>)
```

## Analyze 示例

```python
func.pow(2, 10)

┌────────┐
│ 1024.0  │
└────────┘
```

## SQL 语法

```sql
POW(<x>, <y>)
```

## SQL 示例

```sql
SELECT POW(2, 10);

┌────────┐
│ 1024.0  │
└────────┘
```
