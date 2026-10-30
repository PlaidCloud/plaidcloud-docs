---
title: LOG (Lakehouse v2)
description: LOG — 指定した底に対する数値の対数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/log.md
---

指定した底に対する数値の対数を返します。

## Analyzeの構文

```python
func.log(<base>, <x>)
```

## Analyzeの例

```python
func.log(10, 100)

┌─────┐
│ 2.0  │
└─────┘
```

## SQLの構文

```sql
LOG(<base>, <x>)
```

## SQLの例

```sql
SELECT LOG(10, 100);

┌─────┐
│ 2.0  │
└─────┘
```
