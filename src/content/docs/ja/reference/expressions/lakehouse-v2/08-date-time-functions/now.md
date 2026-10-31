---
title: NOW (Lakehouse v2)
description: NOW — 現在の日付と時刻を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/now.md
---

現在の日付と時刻を返します。

## Analyzeの構文

```python
func.now()
```

## Analyzeの例

```python
func.now()

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## SQLの構文

```sql
NOW()
```

## SQLの例

```sql
SELECT NOW();

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
