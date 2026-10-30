---
title: 날짜 차이 (Lakehouse v1)
description: 날짜 차이 — PlaidCloud Lakehouse는 아직 date_diff 함수를 제공하지 않지만 날짜 산술 연산을 지원합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-diff.md
---

PlaidCloud Lakehouse는 아직 `date_diff` 함수를 제공하지 않지만, 날짜와 시간에 대한 직접 산술 연산을 지원합니다. 예를 들어 `TO_DATE(NOW())-2` 식을 사용하면 이틀 전 날짜를 구할 수 있습니다.

PlaidCloud Lakehouse에서는 이처럼 날짜와 시간을 직접 다룰 수 있어 날짜 및 시간 계산을 편리하고 유연하게 처리할 수 있습니다. 아래 예시를 참조하십시오.

```sql
CREATE TABLE tasks (
  task_name VARCHAR(50),
  start_date DATE,
  end_date DATE
);

INSERT INTO tasks (task_name, start_date, end_date)
VALUES
  ('Task 1', '2023-06-15', '2023-06-20'),
  ('Task 2', '2023-06-18', '2023-06-25'),
  ('Task 3', '2023-06-20', '2023-06-23');

SELECT task_name, end_date - start_date AS duration
FROM tasks;

task_name|duration|
---------+--------+
Task 1   |       5|
Task 2   |       7|
Task 3   |       3|
```
