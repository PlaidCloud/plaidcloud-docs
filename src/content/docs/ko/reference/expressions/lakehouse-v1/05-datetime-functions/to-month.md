---
title: TO_MONTH (Lakehouse v1)
description: TO_MONTH — 날짜 또는 날짜/시간(타임스탬프/datetime)을 월 번호를 담은 UInt8 숫자로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-month.md
---

날짜 또는 날짜/시간(타임스탬프/datetime)을 월 번호(1-12)를 담은 UInt8 숫자로 변환합니다.

## Analyze 구문

```python
func.to_month(<expr>)
```

## Analyze 예시

```python
func.now(), func.to_month(func.now()), func.month(func.now())

┌─────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_month(func.now()) │ func.month(func.now()) │
├────────────────────────────┼───────────────────────────┼────────────────────────┤
│ 2024-03-14 23:34:02.161291 │                         3 │                      3 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
TO_MONTH(<expr>)
```

## 인수

| 인수 | 설명    |
|-----------|----------------|
| `<expr>`  | 날짜/타임스탬프 |

## 별칭

- [MONTH](../month)

## 반환 형식

 `TINYINT`

## SQL 예시

```sql
SELECT NOW(), TO_MONTH(NOW()), MONTH(NOW());

┌─────────────────────────────────────────────────────────────┐
│            now()           │ to_month(now()) │ month(now()) │
├────────────────────────────┼─────────────────┼──────────────┤
│ 2024-03-14 23:34:02.161291 │               3 │            3 │
└─────────────────────────────────────────────────────────────┘
```
