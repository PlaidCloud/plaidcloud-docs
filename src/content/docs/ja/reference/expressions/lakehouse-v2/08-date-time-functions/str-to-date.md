---
title: STR_TO_DATE (Lakehouse v2)
description: STR_TO_DATE — 書式文字列を使用して文字列を日付に解析します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/str-to-date.md
---

書式文字列を使用して文字列を日付に解析します。

## Analyzeの構文

```python
func.str_to_date(<str>, <format>)
```

## Analyzeの例

```python
func.str_to_date('Jun 15 2024', '%b %d %Y')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQLの構文

```sql
STR_TO_DATE(<str>, <format>)
```

## SQLの例

```sql
SELECT STR_TO_DATE('Jun 15 2024', '%b %d %Y');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
