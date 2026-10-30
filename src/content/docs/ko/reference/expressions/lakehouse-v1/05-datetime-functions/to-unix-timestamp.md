---
title: TO_UNIX_TIMESTAMP (Lakehouse v1)
description: TO_UNIX_TIMESTAMP — 날짜/시간 형식의 타임스탬프를 Unix 타임스탬프 형식으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-unix-timestamp.md
---

날짜/시간 형식의 타임스탬프를 Unix 타임스탬프 형식으로 변환합니다. Unix 타임스탬프는 1970년 1월 1일 00:00:00 UTC 이후 경과한 초 수를 나타냅니다.

## Analyze 구문

```python
func.to_unix_timestamp(<expr>)
```

## Analyze 예제

```python
func.to_unix_timestamp('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_unix_timestamp('2023-11-12 09:38:18.165575')           │
│                          UInt32                                │
├────────────────────────────────────────────────────────────────┤
│                                                     1699781898 │
└────────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
TO_UNIX_TIMESTAMP(<expr>)
```

## 인수

| 인수 | 설명 |
| ----------- | ------------------- |
| `<expr>`    | Timestamp           |

타임스탬프 데이터 형식에 대한 자세한 내용은 Date & Time을 참조하십시오.

## 반환 형식

`BIGINT`

## SQL 예제

```sql
SELECT
  to_unix_timestamp('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────────────┐
│ to_unix_timestamp('2023-11-12 09:38:18.165575') │
│                      UInt32                     │
├─────────────────────────────────────────────────┤
│                                      1699781898 │
└─────────────────────────────────────────────────┘
```
