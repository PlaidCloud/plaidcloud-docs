---
title: LOCALTIMESTAMP (Lakehouse v2)
description: LOCALTIMESTAMP — 現在の日付と時刻を返します。`NOW` の別名です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/localtimestamp.md
---

現在の日付と時刻を返します。`NOW` の別名です。

## Analyzeの構文

```python
func.localtimestamp()
```

## Analyzeの例

```python
func.localtimestamp()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## SQLの構文

```sql
LOCALTIMESTAMP()
```

## SQLの例

```sql
SELECT LOCALTIMESTAMP();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
