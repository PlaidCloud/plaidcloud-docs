---
title: STR2DATE (Lakehouse v2)
description: STR2DATE — 書式文字列を使用して文字列を日付に解析します。`STR_TO_DATE` のエイリアスです。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/str2date.md
---

書式文字列を使用して文字列を日付に解析します。`STR_TO_DATE` のエイリアスです。

## Analyzeの構文

```python
func.str2date(<str>, <format>)
```

## Analyzeの例

```python
func.str2date('2024/06/15', '%Y/%m/%d')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQLの構文

```sql
STR2DATE(<str>, <format>)
```

## SQLの例

```sql
SELECT STR2DATE('2024/06/15', '%Y/%m/%d');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
