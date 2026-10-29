---
title: ARG_MIN (Lakehouse v1)
description: ARG_MIN — val 값이 최소일 때의 arg 값을 계산합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-arg-min.md
---

`val` 값이 최소일 때의 `arg` 값을 계산합니다. `val`의 최솟값에 해당하는 서로 다른 `arg` 값이 여러 개이면 처음 만나는 값을 반환합니다.

## Analyze 구문

```python
func.arg_min(<expr>)
```

## Analyze 예제

```python
func.arg_min(table.name, table.score).alias('student_name')

| student_name |
|--------------|
| Charlie      |
```

## SQL 구문

```sql
ARG_MIN(<arg>, <val>)
```

## 인수

| 인수 | 설명 |
|-----------|---------------------------------------------------------------------------------------------------|
| `<arg>`   | PlaidCloud Lakehouse가 지원하는 모든 데이터 형식의 인수 |
| `<val>`   | PlaidCloud Lakehouse가 지원하는 모든 데이터 형식의 값 |

## 반환 형식

`val` 값이 최소일 때의 `arg` 값입니다.

 `arg` 형식과 일치합니다.

## SQL 예제

id, name, score 열이 있는 students 테이블을 만들고 데이터를 삽입합니다.
```sql
CREATE TABLE students (
  id INT,
  name VARCHAR,
  score INT
);

INSERT INTO students (id, name, score) VALUES
  (1, 'Alice', 80),
  (2, 'Bob', 75),
  (3, 'Charlie', 90),
  (4, 'Dave', 80);
```

이제 ARG_MIN을 사용하여 점수가 가장 낮은 학생의 이름을 찾을 수 있습니다.
```sql
SELECT ARG_MIN(name, score) AS student_name
FROM students;
```

결과:
```sql
| student_name |
|--------------|
| Charlie      |
```
