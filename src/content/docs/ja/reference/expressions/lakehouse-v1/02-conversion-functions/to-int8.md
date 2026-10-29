---
title: TO_INT8 (Lakehouse v1)
description: TO_INT8 — 値をINT8データ型に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-int8.md
---

値をINT8データ型に変換します。

## Analyzeの構文

```python
func.to_int8( <expr> )
```

## Analyzeの例

```python
func.to_int8('123')

┌─────────────────────┐
│ func.to_int8('123') │
├─────────────────────┤
│                 123 │
└─────────────────────┘
```

## SQLの構文

```sql
TO_INT8( <expr> )
```

## SQLの例

```sql
SELECT TO_INT8('123');

┌────────────────┐
│ to_int8('123') │
│      UInt8     │
├────────────────┤
│            123 │
└────────────────┘
```
