---
title: TO_YYYYMMDDHH (Lakehouse v1)
description: TO_YYYYMMDDHH — 지정한 날짜 또는 타임스탬프를 "YYYYMMDDHH" 형식의 문자열 표현으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymmddhh.md
---

지정한 날짜 또는 타임스탬프를 "YYYYMMDDHH"(연, 월, 일, 시) 형식의 문자열 표현으로 변환합니다.

## Analyze 구문

```python
func.to_yyyymmddhh(<expr>)
```

## Analyze 예제

```python
func.to_yyyymmddhh('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────────┐
│ func.to_yyyymmddhh('2023-11-12 09:38:18.165575') │
│                   UInt32                         │
├──────────────────────────────────────────────────┤
│                                       2023111209 │
└──────────────────────────────────────────────────┘
```

## SQL 구문

```sql
TO_YYYYMMDDHH(<expr>)
```

## 인수

| 인수 | 설명 |
|-----------|---------------|
| `<expr>`  | date/datetime |

## 반환 형식

"YYYYMMDDHH" 형식의 부호 없는 64비트 정수(UInt64)를 반환합니다.

## SQL 예제

```sql
SELECT
  to_yyyymmddhh('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────────┐
│ to_yyyymmddhh('2023-11-12 09:38:18.165575') │
│                    UInt32                   │
├─────────────────────────────────────────────┤
│                                  2023111209 │
└─────────────────────────────────────────────┘
```
