---
title: TIME_TO_SEC (Lakehouse v2)
description: TIME_TO_SEC — 時刻値を秒数に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/time-to-sec.md
---

時刻値を秒数に変換します。

## Analyzeの構文

```python
func.time_to_sec(<time>)
```

## Analyzeの例

```python
func.time_to_sec('01:01:01')

┌──────┐
│ 3661  │
└──────┘
```

## SQLの構文

```sql
TIME_TO_SEC(<time>)
```

## SQLの例

```sql
SELECT TIME_TO_SEC('01:01:01');

┌──────┐
│ 3661  │
└──────┘
```
