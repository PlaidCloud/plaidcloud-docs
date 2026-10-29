---
title: CURTIME (Lakehouse v2)
description: CURTIME — 現在の時刻を返します。`CURRENT_TIME` の別名です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/curtime.md
---

現在の時刻を返します。`CURRENT_TIME` の別名です。

## Analyzeの構文

```python
func.curtime()
```

## Analyzeの例

```python
func.curtime()

┌────────────┐
│ '14:30:00'  │
└────────────┘
```

## SQLの構文

```sql
CURTIME()
```

## SQLの例

```sql
SELECT CURTIME();

┌──────────┐
│ 14:30:00  │
└──────────┘
```
