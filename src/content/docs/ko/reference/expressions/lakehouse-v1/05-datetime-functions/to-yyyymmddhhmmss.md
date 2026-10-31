---
title: TO_YYYYMMDDHHMMSS (Lakehouse v1)
description: TO_YYYYMMDDHHMMSS — 날짜 또는 시간이 포함된 날짜(timestamp/datetime)를 UInt64 숫자로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymmddhhmmss.md
---

날짜 또는 시간이 포함된 날짜(timestamp/datetime)를 연도와 월 번호가 담긴 UInt64 숫자(YYYY * 10000000000 + MM * 100000000 + DD * 1000000 + hh * 10000 + mm * 100 + ss)로 변환합니다.

## Analyze 구문

```python
func.to_yyyymmddhhmmss(<expr>)
```

## Analyze 예제

```python
func.to_yyyymmddhhmmss('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────────────┐
│ func.to_yyyymmddhhmmss('2023-11-12 09:38:18.165575') │
│                   UInt64                             │
├──────────────────────────────────────────────────────┤
│                                       20231112092818 │
└──────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
TO_YYYYMMDDHHMMSS(<expr>)
```

## 인수

| 인수 | 설명 |
|-----------|----------------|
| `<expr>`  | date/timestamp |

## 반환 형식

`BIGINT`, `YYYYMMDDhhmmss` 형식으로 반환합니다.

## SQL 예제

```sql
SELECT
  to_yyyymmddhhmmss('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────────────┐
│ to_yyyymmddhhmmss('2023-11-12 09:38:18.165575') │
│                      UInt64                     │
├─────────────────────────────────────────────────┤
│                                  20231112092818 │
└─────────────────────────────────────────────────┘
```
