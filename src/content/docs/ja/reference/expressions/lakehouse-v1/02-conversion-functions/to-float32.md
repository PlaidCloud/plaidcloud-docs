---
title: TO_FLOAT32 (Lakehouse v1)
description: TO_FLOAT32 — 値をFLOAT32データ型に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-float32.md
---

値をFLOAT32データ型に変換します。

## Analyzeの構文

```python
func.to_float32( <expr> )
```

## Analyzeの例

```python
func.to_float32('1.2')

┌─────────────────────────┐
│ func.to_float32('1.2')  │
├─────────────────────────┤
│                     1.2 │
└─────────────────────────┘
```

## SQLの構文

```sql
TO_FLOAT32( <expr> )
```

## SQLの例

```sql
SELECT TO_FLOAT32('1.2');

┌───────────────────┐
│ to_float32('1.2') │
├───────────────────┤
│               1.2 │
└───────────────────┘
```
