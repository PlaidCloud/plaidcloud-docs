---
title: TIMESTAMP_DIFF (Lakehouse v1)
description: TIMESTAMP_DIFF — 두 타임스탬프의 차이를 계산하여 INTERVAL로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/timestamp-diff.md
---

두 타임스탬프의 차이를 계산하여 INTERVAL로 반환합니다.

## Analyze 구문

```python
func.timestamp_diff(<timestamp1>, <timestamp2>)
```

## Analyze 예시

```python
func.timestamp_diff(func.to_timestamp('2025-02-01'), func.to_timestamp('2025-01-01'))
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ func.timestamp_diff(func.to_timestamp('2025-02-01'), func.to_timestamp('2025-01-01'))  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 744:00:00                                                                              │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
TIMESTAMP_DIFF(<timestamp1>, <timestamp2>)
```

## 반환 형식

INTERVAL(`hours:minutes:seconds` 형식)입니다.

## SQL 예시

이 예시는 2025년 2월 1일과 2025년 1월 1일 사이의 시간 차이가 744시간이며, 이는 31일에 해당함을 보여 줍니다.

```sql
SELECT TIMESTAMP_DIFF('2025-02-01'::TIMESTAMP, '2025-01-01'::TIMESTAMP);

┌──────────────────────────────────────────────────────────────────┐
│ timestamp_diff('2025-02-01'::TIMESTAMP, '2025-01-01'::TIMESTAMP) │
├──────────────────────────────────────────────────────────────────┤
│ 744:00:00                                                        │
└──────────────────────────────────────────────────────────────────┘
```
