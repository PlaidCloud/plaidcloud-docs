---
title: TO_INT32 (Lakehouse v1)
description: TO_INT32 — 値をINT32データ型に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-int32.md
---

値をINT32データ型に変換します。

## Analyzeの構文

```python
func.to_int32( <expr> )
```

## Analyzeの例

```python
func.to_int32('123')

┌──────────────────────┐
│ func.to_int32('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## SQLの構文

```sql
TO_INT32( <expr> )
```

## SQLの例

```sql
SELECT TO_INT32('123');

┌─────────────────┐
│ to_int32('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```
