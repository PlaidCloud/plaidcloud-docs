---
title: LOCALTIME (Lakehouse v2)
description: LOCALTIME — 現在の日付と時刻を返します。`NOW` の別名です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/localtime.md
---

現在の日付と時刻を返します。`NOW` の別名です。

## Analyzeの構文

```python
func.localtime()
```

## Analyzeの例

```python
func.localtime()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## SQLの構文

```sql
LOCALTIME()
```

## SQLの例

```sql
SELECT LOCALTIME();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
