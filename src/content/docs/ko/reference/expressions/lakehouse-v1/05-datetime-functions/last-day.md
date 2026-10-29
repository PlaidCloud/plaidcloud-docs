---
title: LAST_DAY (Lakehouse v1)
description: LAST_DAY — 지정한 간격(주, 월, 분기 또는 연)의 마지막 날을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/last-day.md
---

제공된 날짜 또는 타임스탬프를 기준으로 지정한 간격(주, 월, 분기 또는 연)의 마지막 날을 반환합니다.

## Analyze 구문

```python
func.last_day(<date_expression>, <interval>)
```

## Analyze 예시

```python
func.last_day(func.to_date('2024-11-13'), 'month')
┌──────────────────────────────────────────────────────┐
│ func.last_day(func.to_date('2024-11-13'), 'month')   │
├──────────────────────────────────────────────────────┤
│ 2024-11-30                                           │
└──────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
LAST_DAY(<date_expression>, <interval>)
```

| 매개변수           | 설명                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------------------|
| `<date_expression>` | 지정한 간격의 마지막 날을 계산할 DATE 또는 TIMESTAMP 값입니다.                                |
| `<interval>`        | 마지막 날을 찾을 간격 유형입니다. 사용할 수 있는 값은 `week`, `month`, `quarter`, `year`입니다. |

## 반환 형식

날짜입니다.

## SQL 예시

임의의 거래 날짜(예: 2024-11-13)를 기준으로, 항상 월의 마지막 날인 청구일을 구한다고 가정해 보겠습니다.

```sql
SELECT LAST_DAY(to_date('2024-11-13'), month) AS billing_date;

┌──────────────┐
│ billing_date │
├──────────────┤
│ 2024-11-30   │
└──────────────┘
```
