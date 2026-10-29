---
title: TO_UINT32 (Lakehouse v1)
description: TO_UINT32 — 値をUINT32データ型に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-uint32.md
---

値をUINT32データ型に変換します。

## Analyzeの構文

```python
func.to_uint32( <expr> )
```

## Analyzeの例

```python
func.to_uint32('123')

┌───────────────────────┐
│ func.to_uint32('123') │
├───────────────────────┤
│                   123 │
└───────────────────────┘
```

## SQLの構文

```sql
TO_UINT32( <expr> )
```

## SQLの例

```sql
SELECT TO_UINT32('123');

┌──────────────────┐
│ to_uint32('123') │
├──────────────────┤
│              123 │
└──────────────────┘
```
