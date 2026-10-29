---
title: JODATIME_FORMAT (Lakehouse v2)
description: JODATIME_FORMAT — Joda-Time の書式パターンを使用して、日付または日時を書式設定します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/jodatime-format.md
---

Joda-Time の書式パターンを使用して、日付または日時を書式設定します。

## Analyzeの構文

```python
func.jodatime_format(<datetime>, <pattern>)
```

## Analyzeの例

```python
func.jodatime_format('2024-06-15', 'yyyy/MM/dd')

┌──────────────┐
│ '2024/06/15'  │
└──────────────┘
```

## SQLの構文

```sql
JODATIME_FORMAT(<datetime>, <pattern>)
```

## SQLの例

```sql
SELECT JODATIME_FORMAT('2024-06-15', 'yyyy/MM/dd');

┌────────────┐
│ 2024/06/15  │
└────────────┘
```
