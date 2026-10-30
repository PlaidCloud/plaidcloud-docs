---
title: MONTHS_BETWEEN (Lakehouse v1)
description: MONTHS_BETWEEN — date1과 date2 사이의 개월 수를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/months-between.md
---

*date1*과 *date2* 사이의 개월 수를 반환합니다.

## Analyze 구문

```python
func.months_between(<date1>, <date2>)
```

## Analyze 예시

```python
func.months_between(func.to_date('2024-03-15'), func.to_date('2024-02-15'))
┌───────────────────────────────────────────────────────────────────────────────┐
│ func.months_between(func.to_date('2024-03-15'), func.to_date('2024-02-15'))   │
├───────────────────────────────────────────────────────────────────────────────┤
│ 1                                                                             │
└───────────────────────────────────────────────────────────────────────────────┘
```

```python
func.months_between(func.to_date('2024-02-15'), func.to_date('2024-03-15'))
┌───────────────────────────────────────────────────────────────────────────────┐
│ func.months_between(func.to_date('2024-02-15'), func.to_date('2024-03-15'))   │
├───────────────────────────────────────────────────────────────────────────────┤
│ -1                                                                             │
└───────────────────────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
MONTHS_BETWEEN( <date1>, <date2> )
```

## 인수

*date1*과 *date2*는 DATE 형식, TIMESTAMP 형식 또는 두 형식의 혼합일 수 있습니다.

## 반환 형식

이 함수는 다음 규칙에 따라 FLOAT 값을 반환합니다.

- *date1*이 *date2*보다 이전이면 음수 값을, 그렇지 않으면 양수 값을 반환합니다.

    ```sql
    SELECT
        MONTHS_BETWEEN('2024-03-15'::DATE,
                    '2024-02-15'::DATE),
        MONTHS_BETWEEN('2024-02-15'::DATE,
                    '2024-03-15'::DATE);

    -[ RECORD 1 ]-----------------------------------
    months_between('2024-03-15'::date, '2024-02-15'::date): 1
    months_between('2024-02-15'::date, '2024-03-15'::date): -1
    ```

- *date1*과 *date2*가 각각 해당 월의 같은 날이거나 둘 다 해당 월의 마지막 날이면 결과는 정수입니다. 그렇지 않으면 한 달을 31일로 보고 결과의 소수 부분을 계산합니다.

    ```sql
    SELECT
        MONTHS_BETWEEN('2024-02-29'::DATE,
                    '2024-01-29'::DATE),
        MONTHS_BETWEEN('2024-02-29'::DATE,
                    '2024-01-31'::DATE);

    -[ RECORD 1 ]-----------------------------------
    months_between('2024-02-29'::date, '2024-01-29'::date): 1
    months_between('2024-02-29'::date, '2024-01-31'::date): 1

    SELECT
        MONTHS_BETWEEN('2024-08-05'::DATE,
                    '2024-01-01'::DATE);

    -[ RECORD 1 ]-----------------------------------
    months_between('2024-08-05'::date, '2024-01-01'::date): 7.129032258064516
    ```

- *date1*과 *date2*가 같은 날짜이면 시간 구성 요소는 무시하고 0을 반환합니다.

    ```sql
    SELECT
        MONTHS_BETWEEN('2024-08-05'::DATE,
                    '2024-08-05'::DATE),
        MONTHS_BETWEEN('2024-08-05 02:00:00'::TIMESTAMP,
                    '2024-08-05 01:00:00'::TIMESTAMP);

    -[ RECORD 1 ]-----------------------------------
                                months_between('2024-08-05'::date, '2024-08-05'::date): 0
    months_between('2024-08-05 02:00:00'::timestamp, '2024-08-05 01:00:00'::timestamp): 0
    ```
