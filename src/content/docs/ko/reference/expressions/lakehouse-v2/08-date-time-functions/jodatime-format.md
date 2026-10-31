---
title: JODATIME_FORMAT (Lakehouse v2)
description: JODATIME_FORMAT — Joda-Time 형식 패턴을 사용하여 날짜 또는 날짜/시간의 형식을 지정합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/jodatime-format.md
---

Joda-Time 형식 패턴을 사용하여 날짜 또는 날짜/시간의 형식을 지정합니다.

## Analyze 구문

```python
func.jodatime_format(<datetime>, <pattern>)
```

## Analyze 예제

```python
func.jodatime_format('2024-06-15', 'yyyy/MM/dd')

┌──────────────┐
│ '2024/06/15'  │
└──────────────┘
```

## SQL 구문

```sql
JODATIME_FORMAT(<datetime>, <pattern>)
```

## SQL 예제

```sql
SELECT JODATIME_FORMAT('2024-06-15', 'yyyy/MM/dd');

┌────────────┐
│ 2024/06/15  │
└────────────┘
```
