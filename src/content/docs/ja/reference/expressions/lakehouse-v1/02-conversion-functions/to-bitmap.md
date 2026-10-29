---
title: TO_BITMAP (Lakehouse v1)
description: TO_BITMAP — 値をBITMAPデータ型に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-bitmap.md
---

値をBITMAPデータ型に変換します。

## Analyzeの構文

```python
func.to_bitmap( <expr> )
```

## Analyzeの例

```python
func.to_bitmap('1101')

┌─────────────────────────┐
│ func.to_bitmap('1101')  │
├─────────────────────────┤
│ <bitmap binary>         │
└─────────────────────────┘
```

## SQLの構文

```sql
TO_BITMAP( <expr> )
```

## SQLの例

```sql
SELECT TO_BITMAP('1101');

┌───────────────────┐
│ to_bitmap('1101') │
├───────────────────┤
│ <bitmap binary>   │
└───────────────────┘
```
