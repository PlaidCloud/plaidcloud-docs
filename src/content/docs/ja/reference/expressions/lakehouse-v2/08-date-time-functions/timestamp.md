---
title: TIMESTAMP (Lakehouse v2)
description: TIMESTAMP — 日付または文字列を日時に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timestamp.md
---

日付または文字列を日時に変換します。

## Analyzeの構文

```python
func.timestamp(<expr>)
```

## Analyzeの例

```python
func.timestamp('2024-06-15')

┌───────────────────────┐
│ '2024-06-15 00:00:00'  │
└───────────────────────┘
```

## SQLの構文

```sql
TIMESTAMP(<expr>)
```

## SQLの例

```sql
SELECT TIMESTAMP('2024-06-15');

┌─────────────────────┐
│ 2024-06-15 00:00:00  │
└─────────────────────┘
```
