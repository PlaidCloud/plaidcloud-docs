---
title: 윈도우 함수 (Lakehouse v1)
description: "Lakehouse v1 SQL 윈도우 함수: 행 윈도우에 대해 계산합니다 — 순위, 누계, 선행 값(lead), 후행 값(lag)."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/index.md
---

## 개요 

윈도우 함수는 관련된 행의 그룹("윈도우")에 대해 동작합니다.

윈도우 함수는 각 입력 행마다 출력 행을 하나 반환하며, 이 출력은 함수에 전달된 특정 행과 윈도우에 있는 다른 행의 값에 따라 달라집니다.

순서에 민감한 윈도우 함수에는 크게 두 가지 유형이 있습니다.

* `Rank-related functions`: 순위 관련 함수는 행의 "순위"를 기준으로 정보를 나열합니다. 예를 들어 연간 이익이 큰 순서로 매장의 순위를 매기면, 이익이 가장 큰 매장이 1위, 두 번째로 이익이 큰 매장이 2위가 되는 식입니다.

* `Window frame functions`: 윈도우 프레임 함수를 사용하면 윈도우에 있는 행의 일부에 대해 누계나 이동 평균 계산과 같은 롤링 연산을 수행할 수 있습니다.

## 윈도우를 지원하는 함수 목록

아래 목록은 모든 윈도우 함수를 보여 줍니다.

| 함수 이름                                                         | 범주     | 윈도우 | 윈도우 프레임 | 비고 |
|-----------------------------------------------------------------------|--------------|--------|--------------|-------|
| [ARRAY_AGG](../07-aggregate-functions/aggregate-array-agg)            | 일반      | ✔      |              |       |
| [AVG](../07-aggregate-functions/aggregate-avg)                        | 일반      | ✔      | ✔            |       |
| [AVG_IF](../07-aggregate-functions/aggregate-avg-if)                  | 일반      | ✔      | ✔            |       |
| [COUNT](../07-aggregate-functions/aggregate-count)                    | 일반      | ✔      | ✔            |       |
| [COUNT_IF](../07-aggregate-functions/aggregate-count-if)              | 일반      | ✔      | ✔            |       |
| [COVAR_POP](../07-aggregate-functions/aggregate-covar-pop)            | 일반      | ✔      |              |       |
| [COVAR_SAMP](../07-aggregate-functions/aggregate-covar-samp)          | 일반      | ✔      |              |       |
| [MAX](../07-aggregate-functions/aggregate-max)                        | 일반      | ✔      | ✔            |       |
| [MAX_IF](../07-aggregate-functions/aggregate-max-if)                  | 일반      | ✔      | ✔            |       |
| [MIN](../07-aggregate-functions/aggregate-min)                        | 일반      | ✔      | ✔            |       |
| [MIN_IF](../07-aggregate-functions/aggregate-min-if)                  | 일반      | ✔      | ✔            |       |
| [STDDEV_POP](../07-aggregate-functions/aggregate-stddev-pop)          | 일반      | ✔      | ✔            |       |
| [STDDEV_SAMP](../07-aggregate-functions/aggregate-stddev-samp)        | 일반      | ✔      | ✔            |       |
| [MEDIAN](../07-aggregate-functions/aggregate-median)                  | 일반      | ✔      | ✔            |       |
| [QUANTILE_CONT](../07-aggregate-functions/aggregate-quantile-cont)    | 일반      | ✔      | ✔            |       |
| [QUANTILE_DISC](../07-aggregate-functions/aggregate-quantile-disc)    | 일반      | ✔      | ✔            |       |
| [KURTOSIS](../07-aggregate-functions/aggregate-kurtosis)              | 일반      | ✔      | ✔            |       |
| [SKEWNESS](../07-aggregate-functions/aggregate-skewness)              | 일반      | ✔      | ✔            |       |
| [SUM](../07-aggregate-functions/aggregate-sum)                        | 일반      | ✔      | ✔            |       |
| [SUM_IF](../07-aggregate-functions/aggregate-sum-if)                  | 일반      | ✔      | ✔            |       |
| [CUME_DIST](cume-dist)                                                | 순위 관련 | ✔      |              |       |
| [PERCENT_RANK](percent-rank/)                                         | 순위 관련 | ✔      | ✔            |       |
| [DENSE_RANK](dense-rank)                                              | 순위 관련 | ✔      | ✔            |       |
| [RANK](rank)                                                          | 순위 관련 | ✔      | ✔            |       |
| [ROW_NUMBER](row-number)                                              | 순위 관련 | ✔      |              |       |
| [NTILE](ntile)                                                        | 순위 관련 | ✔      |              |       |
| [FIRST_VALUE](first-value)                                            | 순위 관련  | ✔     | ✔            |       |
| [FIRST](first)                                                        | 순위 관련 	| ✔     | ✔            |       |
| [LAST_VALUE](last-value)                                              | 순위 관련 	| ✔     | ✔            |       |
| [LAST](last)                                                          | 순위 관련 	| ✔     | ✔            |       |
| [NTH_VALUE](nth-value)                                                | 순위 관련 	| ✔     | ✔            |       |
| [LEAD](lead)                                                          | 순위 관련 	| ✔     |              |       |
| [LAG](lag)                                                            | 순위 관련 	| ✔     |              |       |

## 윈도우 구문

```sql
<function> ( [ <arguments> ] ) OVER ( { named window | inline window } )

named window ::=
    { window_name | ( window_name ) }

inline window ::=
    [ PARTITION BY <expression_list> ]
    [ ORDER BY <expression_list> ]
    [ window frame ]
```
`named window`는 `SELECT` 문의 `WINDOW` 절에서 정의하는 윈도우입니다. 예: `SELECT a, SUM(a) OVER w FROM t WINDOW w AS ( inline window )`.

`<function>`은 ([집계 함수](../07-aggregate-functions), 순위 함수, 값 함수) 중 하나입니다.

`OVER` 절은 함수를 윈도우 함수로 사용한다는 것을 지정합니다.

`PARTITION BY` 하위 절을 사용하면 행을 도시별, 연도별 등의 하위 그룹으로 묶을 수 있습니다. `PARTITION BY` 절은 선택 사항입니다. 행을 하위 그룹으로 나누지 않고 전체 행 그룹을 분석할 수 있습니다.

`ORDER BY` 절은 윈도우 안에서 행을 정렬합니다. 

`window frame` 절은 윈도우 프레임 유형과 윈도우 프레임 범위를 지정합니다. `window frame` 절은 선택 사항입니다. `window frame` 절을 생략하면 기본 윈도우 프레임 유형은 `RANGE`이고 기본 윈도우 프레임 범위는 `UNBOUNDED PRECEDING AND CURRENT ROW`입니다.


## 윈도우 프레임 구문

`window frame`은 다음 유형 중 하나일 수 있습니다.

```sql
cumulativeFrame ::=
    {
       { ROWS | RANGE } BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
     | { ROWS | RANGE } BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING
    }
```

```sql
slidingFrame ::=
    {
       ROWS BETWEEN <N> { PRECEDING | FOLLOWING } AND <N> { PRECEDING | FOLLOWING }
     | ROWS BETWEEN UNBOUNDED PRECEDING AND <N> { PRECEDING | FOLLOWING }
     | ROWS BETWEEN <N> { PRECEDING | FOLLOWING } AND UNBOUNDED FOLLOWING
    }
```


## SQL 예제

**테이블 만들기**
```sql
CREATE TABLE employees (
  employee_id INT,
  first_name VARCHAR,
  last_name VARCHAR,
  department VARCHAR,
  salary INT
);
```

**데이터 삽입**
```sql
INSERT INTO employees (employee_id, first_name, last_name, department, salary) VALUES
  (1, 'John', 'Doe', 'IT', 75000),
  (2, 'Jane', 'Smith', 'HR', 85000),
  (3, 'Mike', 'Johnson', 'IT', 90000),
  (4, 'Sara', 'Williams', 'Sales', 60000),
  (5, 'Tom', 'Brown', 'HR', 82000),
  (6, 'Ava', 'Davis', 'Sales', 62000),
  (7, 'Olivia', 'Taylor', 'IT', 72000),
  (8, 'Emily', 'Anderson', 'HR', 77000),
  (9, 'Sophia', 'Lee', 'Sales', 58000),
  (10, 'Ella', 'Thomas', 'IT', 67000);
```

**예제 1: 급여를 기준으로 직원 순위 매기기**

이 예제에서는 RANK() 함수를 사용하여 급여가 높은 순서로 직원의 순위를 매깁니다. 급여가 가장 높은 직원이 1위가 되고, 급여가 가장 낮은 직원이 가장 큰 순위 번호를 받습니다.
```sql
SELECT employee_id, first_name, last_name, department, salary, RANK() OVER (ORDER BY salary DESC) AS rank
FROM employees;
```

결과:

| employee_id | first_name | last_name | department | salary | rank |
|-------------|------------|-----------|------------|--------|------|
| 3           | Mike       | Johnson   | IT         | 90000  | 1    |
| 2           | Jane       | Smith     | HR         | 85000  | 2    |
| 5           | Tom        | Brown     | HR         | 82000  | 3    |
| 8           | Emily      | Anderson  | HR         | 77000  | 4    |
| 1           | John       | Doe       | IT         | 75000  | 5    |
| 7           | Olivia     | Taylor    | IT         | 72000  | 6    |
| 10          | Ella       | Thomas    | IT         | 67000  | 7    |
| 6           | Ava        | Davis     | Sales      | 62000  | 8    |
| 4           | Sara       | Williams  | Sales      | 60000  | 9    |
| 9           | Sophia     | Lee       | Sales      | 58000  | 10   |



**예제 2: 부서별 총 급여 계산**

이 예제에서는 PARTITION BY와 함께 SUM() 함수를 사용하여 부서별로 지급된 총 급여를 계산합니다. 각 행에는 부서와 해당 부서의 총 급여가 표시됩니다.
```sql
SELECT department, SUM(salary) OVER (PARTITION BY department) AS total_salary
FROM employees;
```

결과:

| department | total_salary |
|------------|--------------|
| HR         | 244000       |
| HR         | 244000       |
| HR         | 244000       |
| IT         | 304000       |
| IT         | 304000       |
| IT         | 304000       |
| IT         | 304000       |
| Sales      | 180000       |
| Sales      | 180000       |
| Sales      | 180000       |


**예제 3: 부서별 급여 누계 계산**

이 예제에서는 누적 윈도우 프레임과 함께 SUM() 함수를 사용하여 각 부서 내 급여의 누계를 계산합니다. 누계는 직원의 급여를 employee_id 순으로 정렬한 기준으로 계산합니다.
```sql
SELECT employee_id, first_name, last_name, department, salary, 
       SUM(salary) OVER (PARTITION BY department ORDER BY employee_id
                         ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM employees;
```

결과:

| employee_id | first_name | last_name | department | salary | running_total |
|-------------|------------|-----------|------------|--------|---------------|
| 2           | Jane       | Smith     | HR         | 85000  | 85000         |
| 5           | Tom        | Brown     | HR         | 82000  | 167000        |
| 8           | Emily      | Anderson  | HR         | 77000  | 244000        |
| 1           | John       | Doe       | IT         | 75000  | 75000         |
| 3           | Mike       | Johnson   | IT         | 90000  | 165000        |
| 7           | Olivia     | Taylor    | IT         | 72000  | 237000        |
| 10          | Ella       | Thomas    | IT         | 67000  | 304000        |
| 4           | Sara       | Williams  | Sales      | 60000  | 60000         |
| 6           | Ava        | Davis     | Sales      | 62000  | 122000        |
| 9           | Sophia     | Lee       | Sales      | 58000  | 180000        |
