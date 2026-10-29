---
title: TO_CENTURIES (Lakehouse v1)
description: TO_CENTURIES — 지정한 세기 수를 Interval 형식으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-centuries.md
---

지정한 세기 수를 Interval 형식으로 변환합니다.

- 양의 정수, 0, 음의 정수를 입력으로 받습니다.

## Analyze 구문

```python
func.to_centuries(<centuries>)
```

## Analyze 예제

```python
func.to_centuries(2)
┌──────────────────────────────────────────────────────┐
│ func.to_centuries(2)                                 │
├──────────────────────────────────────────────────────┤
│ 200 years                                            │
└──────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
TO_CENTURIES(<centuries>)
```

## 반환 형식

Interval(년 단위로 표현).

## SQL 예제

```sql
SELECT TO_CENTURIES(2), TO_CENTURIES(0), TO_CENTURIES(-2);

┌───────────────────────────────────────────────────────┐
│ to_centuries(2) │ to_centuries(0) │ to_centuries(- 2) │
├─────────────────┼─────────────────┼───────────────────┤
│ 200 years       │ 00:00:00        │ -200 years        │
└───────────────────────────────────────────────────────┘
```
