---
title: HOUR (Lakehouse v2)
description: HOUR — 日時から時を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/hour.md
---

日時から時を返します。

## Analyzeの構文

```python
func.hour(<datetime>)
```

## Analyzeの例

```python
func.hour('2024-06-15 14:30:00')

┌────┐
│ 14  │
└────┘
```

## SQLの構文

```sql
HOUR(<datetime>)
```

## SQLの例

```sql
SELECT HOUR('2024-06-15 14:30:00');

┌────┐
│ 14  │
└────┘
```
