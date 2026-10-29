---
title: TO_DATE (Lakehouse v2)
description: TO_DATE — 日時を日付に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-date.md
---

日時を日付に変換します。

## Analyzeの構文

```python
func.to_date(<datetime>)
```

## Analyzeの例

```python
func.to_date('2024-06-15 14:30:00')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQLの構文

```sql
TO_DATE(<datetime>)
```

## SQLの例

```sql
SELECT TO_DATE('2024-06-15 14:30:00');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
