---
title: TO_UINT8 (Lakehouse v1)
description: TO_UINT8 — 値をUINT8データ型に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-uint8.md
---

値をUINT8データ型に変換します。

## Analyzeの構文

```python
func.to_uint8( <expr> )
```

## Analyzeの例

```python
func.to_uint8('123')

┌──────────────────────┐
│ func.to_uint8('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## SQLの構文

```sql
TO_UINT8( <expr> )
```

## SQLの例

```sql
SELECT TO_UINT8('123');

┌─────────────────┐
│ to_uint8('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```
