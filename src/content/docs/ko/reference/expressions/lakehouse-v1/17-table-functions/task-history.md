---
title: TASK_HISTORY (Lakehouse v1)
description: TASK_HISTORY — 지정한 변수에 따라 작업 실행 이력을 표시합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/task-history.md
---

지정한 변수에 따라 작업 실행 이력을 표시합니다.

## SQL 구문
```sql
TASK_HISTORY(
      [ SCHEDULED_TIME_RANGE_START => <constant_expr> ]
      [, SCHEDULED_TIME_RANGE_END => <constant_expr> ]
      [, RESULT_LIMIT => <integer> ]
      [, TASK_NAME => '<string>' ]
      [, ERROR_ONLY => { TRUE | FALSE } ]
      [, ROOT_TASK_ID => '<string>'] )
```



## 인수

모든 인수는 선택 사항입니다.

`SCHEDULED_TIME_RANGE_START => <constant_expr>`, `SCHEDULED_TIME_RANGE_END => <constant_expr>`

작업 실행이 예약된 시간 범위(TIMESTAMP_LTZ 형식)이며, 최근 7일 이내여야 합니다. 시간 범위가 최근 7일 이내가 아니면 오류가 반환됩니다.

* `SCHEDULED_TIME_RANGE_END`를 지정하지 않으면 이미 완료되었거나, 현재 실행 중이거나, 미래에 예약된 작업을 반환합니다.
* `SCHEDULED_TIME_RANGE_END`가 CURRENT_TIMESTAMP이면 이미 완료되었거나 현재 실행 중인 작업을 반환합니다. 현재 시간 직전에 실행된 작업은 여전히 예약된 것으로 식별될 수 있습니다.
* 이미 완료되었거나 현재 실행 중인 작업만 쿼리하려면 필터로 `WHERE query_id IS NOT NULL`을 포함하십시오. TASK_HISTORY 출력의 QUERY_ID 열은 작업이 실행을 시작한 경우에만 채워집니다.

시작 시간이나 종료 시간을 지정하지 않으면 지정한 RESULT_LIMIT 값까지 가장 최근 작업을 반환합니다.

`RESULT_LIMIT => <integer>`

함수가 반환하는 최대 행 수를 지정하는 숫자입니다.

일치하는 행 수가 이 제한보다 크면 지정한 제한까지 타임스탬프가 가장 최근인 작업 실행을 반환합니다.

범위: `1` ~ `10000`

기본값: `100`.

`TASK_NAME => <string>`

작업을 지정하는, 대소문자를 구분하지 않는 문자열입니다. 정규화되지 않은 작업 이름만 지원합니다. 지정한 작업의 실행만 반환합니다. 이름이 같은 작업이 여러 개이면 함수는 해당 작업 각각의 이력을 반환합니다.

`ERROR_ONLY => { TRUE | FALSE }`

TRUE로 설정하면 이 함수는 실패했거나 취소된 작업 실행만 반환합니다.

`ROOT_TASK_ID => <string>`

작업 그래프에서 루트 작업의 고유 식별자입니다. 이 ID는 동일한 작업에 대한 SHOW TASKS 출력의 ID 열 값과 일치합니다. ROOT_TASK_ID를 지정하면 루트 작업과 작업 그래프에 포함된 모든 하위 작업의 이력을 표시합니다.

## 사용 참고 사항
* 이 함수는 RESULT_LIMIT 인수 값으로 설정된 최대 10,000개 행을 반환합니다. 기본값은 100입니다.
* 이 함수는 ACCOUNTADMIN 역할에 대해서만 결과를 반환합니다.


## SQL 예제

```sql
SELECT
  *
FROM TASK_HISTORY() order by scheduled_time;
```
위 SQL 쿼리는 TASK_HISTORY 함수에서 모든 작업 이력 레코드를 가져와 scheduled_time 열 기준으로 정렬합니다(최대 10,000개).



```sql
SELECT *
  FROM TASK_HISTORY(
    SCHEDULED_TIME_RANGE_START=>TO_TIMESTAMP('2022-01-02T01:12:00-07:00'),
    SCHEDULED_TIME_RANGE_END=>TO_TIMESTAMP('2022-01-02T01:12:30-07:00'))
```

위 SQL 쿼리는 예약 시간 범위가 '2022-01-02T01:12:00-07:00'에 시작하여 '2022-01-02T01:12:30-07:00'에 끝나는 모든 작업 이력 레코드를 TASK_HISTORY 함수에서 가져옵니다. 즉, 이 30초 시간 창 안에 실행되도록 예약된 작업을 반환하며, 결과에는 이 조건에 일치하는 작업의 세부 정보가 포함됩니다.
