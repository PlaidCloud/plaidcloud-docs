---
title: TO_SECOND (Lakehouse v1)
description: TO_SECOND — 날짜/시간(타임스탬프/datetime)을 해당 분의 초(0-59)를 담은 UInt8 숫자로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-second.md
---

날짜/시간(타임스탬프/datetime)을 해당 분의 초(0-59)를 담은 UInt8 숫자로 변환합니다.

## Analyze 구문

```python
func.to_second(<expr>)
```

## Analyze 예시

```python
func.to_second('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────┐
│ func.to_second('2023-11-12 09:38:18.165575') │
│                   UInt8                      │
├──────────────────────────────────────────────┤
│                                           18 │
└──────────────────────────────────────────────┘
```

## SQL 구문

```sql
TO_SECOND(<expr>)
```

## 인수

| 인수 | 설명 |
|-----------|-------------|
| `<expr>`  | 타임스탬프   |

## 반환 형식

`TINYINT`

## SQL 예시

```sql
SELECT
    to_second('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ to_second('2023-11-12 09:38:18.165575') │
│                  UInt8                  │
├─────────────────────────────────────────┤
│                                      18 │
└─────────────────────────────────────────┘
```
