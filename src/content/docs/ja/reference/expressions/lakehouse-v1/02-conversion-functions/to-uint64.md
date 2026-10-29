---
title: TO_UINT64 (Lakehouse v1)
description: TO_UINT64 — 値をUINT64データ型に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-uint64.md
---

値をUINT64データ型に変換します。

## Analyzeの構文

```python
func.to_uint64( <expr> )
```

## Analyzeの例

```python
func.to_uint64('123')

┌───────────────────────┐
│ func.to_uint64('123') │
├───────────────────────┤
│                   123 │
└───────────────────────┘
```

## SQLの構文

```sql
TO_UINT64( <expr> )
```

## SQLの例

```sql
SELECT TO_UINT64('123');

┌──────────────────┐
│ to_uint64('123') │
├──────────────────┤
│              123 │
└──────────────────┘
```
