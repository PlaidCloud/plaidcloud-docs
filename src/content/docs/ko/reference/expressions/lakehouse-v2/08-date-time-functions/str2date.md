---
title: STR2DATE (Lakehouse v2)
description: STR2DATE — 형식 문자열을 사용하여 문자열을 날짜로 파싱합니다. `STR_TO_DATE`의 별칭입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/str2date.md
---

형식 문자열을 사용하여 문자열을 날짜로 파싱합니다. `STR_TO_DATE`의 별칭입니다.

## Analyze 구문

```python
func.str2date(<str>, <format>)
```

## Analyze 예제

```python
func.str2date('2024/06/15', '%Y/%m/%d')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL 구문

```sql
STR2DATE(<str>, <format>)
```

## SQL 예제

```sql
SELECT STR2DATE('2024/06/15', '%Y/%m/%d');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
