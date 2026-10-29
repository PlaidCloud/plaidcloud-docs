---
title: STR_TO_DATE (Lakehouse v2)
description: STR_TO_DATE — 형식 문자열을 사용하여 문자열을 날짜로 파싱합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/str-to-date.md
---

형식 문자열을 사용하여 문자열을 날짜로 파싱합니다.

## Analyze 구문

```python
func.str_to_date(<str>, <format>)
```

## Analyze 예제

```python
func.str_to_date('Jun 15 2024', '%b %d %Y')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL 구문

```sql
STR_TO_DATE(<str>, <format>)
```

## SQL 예제

```sql
SELECT STR_TO_DATE('Jun 15 2024', '%b %d %Y');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
