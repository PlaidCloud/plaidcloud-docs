---
title: TO_INT16 (Lakehouse v1)
description: TO_INT16 — 値をINT16データ型に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-int16.md
---

値をINT16データ型に変換します。

## Analyzeの構文

```python
func.to_int16( <expr> )
```

## Analyzeの例

```python
func.to_int16('123')

┌──────────────────────┐
│ func.to_int16('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## SQLの構文

```sql
TO_INT16( <expr> )
```

## SQLの例

```sql
SELECT TO_INT16('123');

┌─────────────────┐
│ to_int16('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```
