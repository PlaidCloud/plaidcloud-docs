---
title: FROM_DAYS (Lakehouse v2)
description: FROM_DAYS — 日数を日付に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/from-days.md
---

日数を日付に変換します。

## Analyzeの構文

```python
func.from_days(<n>)
```

## Analyzeの例

```python
func.from_days(738886)

┌──────────────┐
│ '2024-01-01'  │
└──────────────┘
```

## SQLの構文

```sql
FROM_DAYS(<n>)
```

## SQLの例

```sql
SELECT FROM_DAYS(738886);

┌────────────┐
│ 2024-01-01  │
└────────────┘
```
