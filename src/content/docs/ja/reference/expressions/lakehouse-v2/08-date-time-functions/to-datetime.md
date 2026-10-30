---
title: TO_DATETIME (Lakehouse v2)
description: TO_DATETIME — 値を日時に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-datetime.md
---

値を日時に変換します。

## Analyzeの構文

```python
func.to_datetime(<expr>)
```

## Analyzeの例

```python
func.to_datetime('2024-06-15')

┌───────────────────────┐
│ '2024-06-15 00:00:00'  │
└───────────────────────┘
```

## SQLの構文

```sql
TO_DATETIME(<expr>)
```

## SQLの例

```sql
SELECT TO_DATETIME('2024-06-15');

┌─────────────────────┐
│ 2024-06-15 00:00:00  │
└─────────────────────┘
```
