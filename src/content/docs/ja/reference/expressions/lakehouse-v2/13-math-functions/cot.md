---
title: COT (Lakehouse v2)
description: COT — ラジアンで指定した数値の余接を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cot.md
---

ラジアンで指定した数値の余接を返します。

## Analyzeの構文

```python
func.cot(<x>)
```

## Analyzeの例

```python
func.cot(1)

┌────────────────────┐
│ 0.6420926159343306  │
└────────────────────┘
```

## SQLの構文

```sql
COT(<x>)
```

## SQLの例

```sql
SELECT COT(1);

┌────────────────────┐
│ 0.6420926159343306  │
└────────────────────┘
```
