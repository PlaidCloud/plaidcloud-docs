---
title: TIMESTAMPADD (Lakehouse v2)
description: TIMESTAMPADD — 日時に指定した時間間隔を加算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timestampadd.md
---

日時に指定した時間間隔を加算します。

## Analyzeの構文

```python
func.timestampadd(<unit>, <n>, <datetime>)
```

## Analyzeの例

```python
func.timestampadd('DAY', 7, '2024-01-01')

┌──────────────┐
│ '2024-01-08'  │
└──────────────┘
```

## SQLの構文

```sql
TIMESTAMPADD(<unit>, <n>, <datetime>)
```

## SQLの例

```sql
SELECT TIMESTAMPADD(DAY, 7, '2024-01-01');

┌────────────┐
│ 2024-01-08  │
└────────────┘
```
