---
title: ROW_NUMBER (Lakehouse v1)
description: ROW_NUMBER — 결과 파티션 내의 각 행에 임시 순차 번호를 할당합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/row-number.md
---

결과 집합의 파티션 내 각 행에 임시 순차 번호를 할당하며, 각 파티션의 첫 번째 행이 1부터 시작합니다.

## Analyze 구문

```python
func.row_number().over(partition_by=[<columns>], order_by=[<columns>])
```

## Analyze 예제

```python
table.employee_id, table.first_name, table.last_name, table.department, table.salary, func.row_number().over(partition=table.department, order_by=table.salary).alias('row_num')

┌──────────────────────────────────────────────────────────────────────────────────────────────────────┐
│   employee_id   │    first_name    │     last_name    │    department    │      salary     │ row_num │
├─────────────────┼──────────────────┼──────────────────┼──────────────────┼─────────────────┼─────────┤
│               2 │ Jane             │ Smith            │ HR               │           85000 │       1 │
│               5 │ Tom              │ Brown            │ HR               │           75000 │       2 │
│               1 │ John             │ Doe              │ IT               │           90000 │       1 │
│               3 │ Mike             │ Johnson          │ IT               │           82000 │       2 │
│               4 │ Sara             │ Williams         │ Sales            │           77000 │       1 │
└──────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
ROW_NUMBER() 
  OVER ( [ PARTITION BY <expr1> [, <expr2> ... ] ]
  ORDER BY <expr3> [ , <expr4> ... ] [ { ASC | DESC } ] )
```

| 매개변수    | 필수 여부 | 설명                                                                                                |
|--------------|-----------|------------------------------------------------------------------------------------------------------------|
| ORDER BY     | 예       | 각 파티션 내 행의 순서를 지정합니다.                                                         |
| ASC / DESC   | 아니요        | 각 파티션 내 정렬 순서를 지정합니다. 기본값은 ASC(오름차순)입니다.                         |
| QUALIFY      | 아니요        | 조건에 따라 행을 필터링합니다.                                                                          |

## SQL 예제

이 예제는 ROW_NUMBER()를 사용하여 각 부서 내 직원에게 급여 내림차순으로 순차 번호를 할당하는 방법을 보여 줍니다.

```sql
-- Prepare the data
CREATE TABLE employees (
  employee_id INT,
  first_name VARCHAR,
  last_name VARCHAR,
  department VARCHAR,
  salary INT
);

INSERT INTO employees (employee_id, first_name, last_name, department, salary) VALUES
  (1, 'John', 'Doe', 'IT', 90000),
  (2, 'Jane', 'Smith', 'HR', 85000),
  (3, 'Mike', 'Johnson', 'IT', 82000),
  (4, 'Sara', 'Williams', 'Sales', 77000),
  (5, 'Tom', 'Brown', 'HR', 75000);

-- Select employee details along with the row number partitioned by department and ordered by salary in descending order.
SELECT
    employee_id,
    first_name,
    last_name,
    department,
    salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS row_num
FROM
    employees;

┌──────────────────────────────────────────────────────────────────────────────────────────────────────┐
│   employee_id   │    first_name    │     last_name    │    department    │      salary     │ row_num │
├─────────────────┼──────────────────┼──────────────────┼──────────────────┼─────────────────┼─────────┤
│               2 │ Jane             │ Smith            │ HR               │           85000 │       1 │
│               5 │ Tom              │ Brown            │ HR               │           75000 │       2 │
│               1 │ John             │ Doe              │ IT               │           90000 │       1 │
│               3 │ Mike             │ Johnson          │ IT               │           82000 │       2 │
│               4 │ Sara             │ Williams         │ Sales            │           77000 │       1 │
└──────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
