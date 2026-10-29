---
title: DATE_ADD (Lakehouse v1)
description: DATE_ADD — 지정한 날짜 또는 날짜/시간에 시간 간격 또는 날짜 간격을 더합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-add.md
---

지정한 날짜 또는 날짜/시간(타임스탬프/datetime)에 시간 간격 또는 날짜 간격을 더합니다.

## Analyze 구문

```python
func.date_add(<unit>, <value>,  <date_or_time_expr>)
```

## Analyze 예시

```python
func.date_add('YEAR', 1, func.to_date('2018-01-02'))
┌──────────────────────────────────────────────────────┐
│ func.date_add('YEAR', 1, func.to_date('2018-01-02')) │
├──────────────────────────────────────────────────────┤
│ 2019-01-02                                           │
└──────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
DATE_ADD(<unit>, <value>,  <date_or_time_expr>)
```
## 인수

| 인수             | 설명                                                                                                       |
|-----------------------|-------------------------------------------------------------------------------------------------------------------|
| `<unit>`              | 다음 값 중 하나여야 합니다. `YEAR`, `QUARTER`, `MONTH`, `DAY`, `HOUR`, `MINUTE`, `SECOND`                 |
| `<value>`             | 더하려는 시간 단위의 수입니다. 예를 들어 2일을 더하려면 2입니다. |
| `<date_or_time_expr>` | `DATE` 또는 `TIMESTAMP` 형식의 값                                                                             |

## 반환 형식

`<date_or_time_expr>` 인수와 같은 형식의 값을 반환합니다.

## SQL 예시

```sql
SELECT date_add(YEAR, 1, to_date('2018-01-02'));
┌───────────────────────────────────────────────────┐
│ DATE_ADD(YEAR, INTERVAL 1, to_date('2018-01-02')) │
├───────────────────────────────────────────────────┤
│ 2019-01-02                                        │
└───────────────────────────────────────────────────┘
```
