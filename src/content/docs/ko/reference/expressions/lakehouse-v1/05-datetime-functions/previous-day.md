---
title: PREVIOUS_DAY (Lakehouse v1)
description: PREVIOUS_DAY — 지정한 날짜 이전에 가장 최근에 있었던 지정 요일의 날짜를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/previous-day.md
---

지정한 날짜 또는 타임스탬프 이전에 가장 최근에 있었던 지정 요일의 날짜를 반환합니다.

## Analyze 구문

```python
func.next_day(date_expression>, <target_day>)
```

## Analyze 예시

```python
func.next_day(func.to_date('2024-11-13'), 'friday')
┌──────────────────────────────────────────────────────┐
│ func.next_day(func.to_date('2024-11-13'), 'friday')  │
├──────────────────────────────────────────────────────┤
│ 2024-11-08                                           │
└──────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
PREVIOUS_DAY(<date_expression>, <target_day>)
```

| 매개변수           | 설명                                                                                                                                                              |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<date_expression>` | 지정한 요일의 이전 날짜를 계산할 `DATE` 또는 `TIMESTAMP` 값입니다.                                                                                 |
| `<target_day>`      | 이전 날짜를 찾을 대상 요일입니다. 사용할 수 있는 값은 `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday`, `sunday`입니다. |

## 반환 형식

날짜입니다.

## SQL 예시

특정 날짜(예: 2024-11-13) 이전의 금요일을 찾아야 하는 경우는 다음과 같습니다.

```sql
SELECT PREVIOUS_DAY(to_date('2024-11-13'), friday) AS last_friday;

┌─────────────┐
│ last_friday │
├─────────────┤
│ 2024-11-08  │
└─────────────┘
```
