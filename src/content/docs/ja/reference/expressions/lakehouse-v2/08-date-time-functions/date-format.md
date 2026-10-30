---
title: DATE_FORMAT (Lakehouse v2)
description: DATE_FORMAT — 書式文字列に従って、日付または日時の値を書式設定します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date-format.md
---

書式文字列に従って、日付または日時の値を書式設定します。

## Analyzeの構文

```python
func.date_format(<date>, <format>)
```

## Analyzeの例

```python
func.date_format('2024-06-15', '%Y/%m/%d')

┌──────────────┐
│ '2024/06/15'  │
└──────────────┘
```

## SQLの構文

```sql
DATE_FORMAT(<date>, <format>)
```

## SQLの例

```sql
SELECT DATE_FORMAT('2024-06-15', '%Y/%m/%d');

┌────────────┐
│ 2024/06/15  │
└────────────┘
```
