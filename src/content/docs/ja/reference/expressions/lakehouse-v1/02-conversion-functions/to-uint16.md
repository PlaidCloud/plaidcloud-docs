---
title: TO_UINT16 (Lakehouse v1)
description: TO_UINT16 — 値をUINT16データ型に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-uint16.md
---

値をUINT16データ型に変換します。

## Analyzeの構文

```python
func.to_uint16( <expr> )
```

## Analyzeの例

```python
func.to_uint16('123')

┌───────────────────────┐
│ func.to_uint16('123') │
├───────────────────────┤
│                   123 │
└───────────────────────┘
```

## SQLの構文

```sql
TO_UINT16( <expr> )
```

## SQLの例

```sql
SELECT TO_UINT16('123');

┌──────────────────┐
│ to_uint16('123') │
├──────────────────┤
│              123 │
└──────────────────┘
```
