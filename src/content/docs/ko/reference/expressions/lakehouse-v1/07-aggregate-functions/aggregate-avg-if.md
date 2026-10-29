---
title: AVG_IF (Lakehouse v1)
description: AVG_IF — 접미사 -If를 모든 집계 함수 이름 뒤에 붙일 수 있습니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-avg-if.md
---

접미사 -If를 모든 집계 함수 이름 뒤에 붙일 수 있습니다. 이 경우 집계 함수는 조건이라는 추가 인수를 받습니다.

## Analyze 구문

```python
func.avg_if(<column>, <cond>)
```

## Analyze 예제

```python
func.avg_if(table.salary, table.department=='IT').alias('avg_salary_it')

| avg_salary_it   |
|-----------------|
|     65000.0     |
```

## SQL 구문
```sql
AVG_IF(<column>, <cond>)
```

## SQL 예제

**테이블을 만들고 샘플 데이터 삽입**
```sql
CREATE TABLE employees (
  id INT,
  salary INT,
  department VARCHAR
);

INSERT INTO employees (id, salary, department)
VALUES (1, 50000, 'HR'),
       (2, 60000, 'IT'),
       (3, 55000, 'HR'),
       (4, 70000, 'IT'),
       (5, 65000, 'IT');
```

**쿼리 데모: IT 부서의 평균 급여 계산**

```sql
SELECT AVG_IF(salary, department = 'IT') AS avg_salary_it
FROM employees;
```

**결과**
```sql
| avg_salary_it   |
|-----------------|
|     65000.0     |
```
