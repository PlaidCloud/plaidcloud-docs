---
title: CURRENT_DATE (Lakehouse v2)
description: CURRENT_DATE — 現在の日付を返します。`CURDATE` の別名です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-date.md
---

現在の日付を返します。`CURDATE` の別名です。

## Analyzeの構文

```python
func.current_date()
```

## Analyzeの例

```python
func.current_date()

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQLの構文

```sql
CURRENT_DATE()
```

## SQLの例

```sql
SELECT CURRENT_DATE();

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
