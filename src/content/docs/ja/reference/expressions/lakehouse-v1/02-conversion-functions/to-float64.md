---
title: TO_FLOAT64 (Lakehouse v1)
description: TO_FLOAT64 — 値をFLOAT64データ型に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-float64.md
---

値をFLOAT64データ型に変換します。

## Analyzeの構文

```python
func.to_float64( <expr> )
```

## Analyzeの例

```python
func.to_float64('1.2')

┌─────────────────────────┐
│ func.to_float64('1.2')  │
├─────────────────────────┤
│                     1.2 │
└─────────────────────────┘
```

## SQLの構文

```sql
TO_FLOAT64( <expr> )
```

## SQLの例

```sql
SELECT TO_FLOAT64('1.2');

┌───────────────────┐
│ to_float64('1.2') │
├───────────────────┤
│               1.2 │
└───────────────────┘
```
