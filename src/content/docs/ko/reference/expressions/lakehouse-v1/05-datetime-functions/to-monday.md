---
title: TO_MONDAY (Lakehouse v1)
description: TO_MONDAY — 날짜 또는 날짜/시간(타임스탬프/datetime)을 가장 가까운 이전 월요일로 내림합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-monday.md
---

날짜 또는 날짜/시간(타임스탬프/datetime)을 가장 가까운 이전 월요일로 내림합니다.
날짜를 반환합니다.

## Analyze 구문

```python
func.to_monday(<expr>)
```

## Analyze 예시

```python
func.to_monday('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_monday('2023-11-12 09:38:18.165575')       │
│                      Date                          │
├────────────────────────────────────────────────────┤
│ 2023-11-06                                         │
└────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
TO_MONDAY(<expr>)
```

## 인수

| 인수   | 설명 |
| ----------- | ----------- |
| `<expr>` | 날짜/타임스탬프 |

## 반환 형식

`DATE`이며, “YYYY-MM-DD” 형식의 날짜를 반환합니다.

## SQL 예시

```sql
SELECT
    to_monday('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ to_monday('2023-11-12 09:38:18.165575') │
│                   Date                  │
├─────────────────────────────────────────┤
│ 2023-11-06                              │
└─────────────────────────────────────────┘
```
