---
title: STR_TO_JODATIME (Lakehouse v2)
description: STR_TO_JODATIME — Joda-Time 형식 패턴을 사용하여 문자열을 날짜/시간 값으로 파싱합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/str-to-jodatime.md
---

Joda-Time 형식 패턴을 사용하여 문자열을 날짜/시간 값으로 파싱합니다.

## Analyze 구문

```python
func.str_to_jodatime(<str>, <pattern>)
```

## Analyze 예제

```python
func.str_to_jodatime('2024/06/15', 'yyyy/MM/dd')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL 구문

```sql
STR_TO_JODATIME(<str>, <pattern>)
```

## SQL 예제

```sql
SELECT STR_TO_JODATIME('2024/06/15', 'yyyy/MM/dd');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
