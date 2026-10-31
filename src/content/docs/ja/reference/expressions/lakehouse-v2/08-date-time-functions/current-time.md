---
title: CURRENT_TIME (Lakehouse v2)
description: CURRENT_TIME — 現在の時刻を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-time.md
---

現在の時刻を返します。

## Analyzeの構文

```python
func.current_time()
```

## Analyzeの例

```python
func.current_time()

┌────────────┐
│ '14:30:00'  │
└────────────┘
```

## SQLの構文

```sql
CURRENT_TIME()
```

## SQLの例

```sql
SELECT CURRENT_TIME();

┌──────────┐
│ 14:30:00  │
└──────────┘
```
