---
title: NEXT_DAY (Lakehouse v1)
description: NEXT_DAY — 지정한 날짜 또는 타임스탬프 이후에 돌아오는 지정 요일의 날짜를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/next-day.md
---

지정한 날짜 또는 타임스탬프 이후에 돌아오는 지정 요일의 날짜를 반환합니다.

## Analyze 구문

```python
func.next_day(date_expression>, <target_day>)
```

## Analyze 예시

```python
func.next_day(func.to_date('2024-11-13'), 'monday')
┌──────────────────────────────────────────────────────┐
│ func.next_day(func.to_date('2024-11-13'), 'monday')  │
├──────────────────────────────────────────────────────┤
│ 2024-11-18                                           │
└──────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
NEXT_DAY(<date_expression>, <target_day>)
```

| 매개변수           | 설명                                                                                                                                                              |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<date_expression>` | 지정한 요일의 다음 날짜를 계산할 `DATE` 또는 `TIMESTAMP` 값입니다.                                                                                 |
| `<target_day>`      | 다음 날짜를 찾을 대상 요일입니다. 사용할 수 있는 값은 `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday`, `sunday`입니다. |

## 반환 형식

날짜입니다.

## SQL 예시

특정 날짜(예: 2024-11-13) 이후의 다음 월요일을 찾으려면 다음과 같이 합니다.

```sql
SELECT NEXT_DAY(to_date('2024-11-13'), monday) AS next_monday;

┌─────────────┐
│ next_monday │
├─────────────┤
│ 2024-11-18  │
└─────────────┘
```
