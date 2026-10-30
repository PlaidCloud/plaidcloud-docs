---
title: CURRENT_TIMEZONE (Lakehouse v2)
description: CURRENT_TIMEZONE — 現在のセッションのタイムゾーンを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/current-timezone.md
---

現在のセッションのタイムゾーンを返します。

## Analyzeの構文

```python
func.current_timezone()
```

## Analyzeの例

```python
func.current_timezone()

┌────────────────────┐
│ 'America/New_York'  │
└────────────────────┘
```

## SQLの構文

```sql
CURRENT_TIMEZONE()
```

## SQLの例

```sql
SELECT CURRENT_TIMEZONE();

┌──────────────────┐
│ America/New_York  │
└──────────────────┘
```
