---
title: MIN_IF (Lakehouse v1)
description: MIN_IF — 접미사 _IF를 모든 집계 함수 이름 뒤에 붙일 수 있습니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-min-if.md
---

접미사 `_IF`를 모든 집계 함수 이름 뒤에 붙일 수 있습니다. 이 경우 집계 함수는 조건이라는 추가 인수를 받습니다.

## Analyze 구문

```python
func.min_if(<column>, <cond>)
```

## Analyze 예제

```python
func.min_if(table.budget, table.departing=='IT').alias('min_it_budget')

| min_it_budget |
|---------------|
|     2000      |
```

## SQL 구문

```sql
MIN_IF(<column>, <cond>)
```

## SQL 예제

**테이블을 만들고 샘플 데이터 삽입**
```sql
CREATE TABLE project_budgets (
  id INT,
  project_id INT,
  department VARCHAR,
  budget FLOAT
);

INSERT INTO project_budgets (id, project_id, department, budget)
VALUES (1, 1, 'HR', 1000),
       (2, 1, 'IT', 2000),
       (3, 1, 'Marketing', 3000),
       (4, 2, 'HR', 1500),
       (5, 2, 'IT', 2500);
```

**쿼리 데모: IT 부서의 최소 예산 찾기**

```sql
SELECT MIN_IF(budget, department = 'IT') AS min_it_budget
FROM project_budgets;
```

**결과**
```sql
| min_it_budget |
|---------------|
|     2000      |
```
