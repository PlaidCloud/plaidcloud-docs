---
title: NEXTVAL (Lakehouse v1)
description: NEXTVAL — 시퀀스에서 다음 값을 가져옵니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/18-sequence-functions/nextval.md
---

시퀀스에서 다음 값을 가져옵니다.

## SQL 구문

```sql
NEXTVAL(<sequence_name>)
```

## 반환 유형

정수.

## SQL 예제

이 예제는 NEXTVAL 함수가 시퀀스와 함께 작동하는 방식을 보여 줍니다.

```sql
CREATE SEQUENCE my_seq;

SELECT
  NEXTVAL(my_seq),
  NEXTVAL(my_seq),
  NEXTVAL(my_seq);

┌─────────────────────────────────────────────────────┐
│ nextval(my_seq) │ nextval(my_seq) │ nextval(my_seq) │
├─────────────────┼─────────────────┼─────────────────┤
│               1 │               2 │               3 │
└─────────────────────────────────────────────────────┘
```

이 예제는 시퀀스와 NEXTVAL 함수를 사용하여 테이블의 행에 고유 식별자를 자동으로 생성하고 할당하는 방법을 보여 줍니다.

```sql
-- Create a new sequence named staff_id_seq
CREATE SEQUENCE staff_id_seq;

-- Create a new table named staff with columns for staff_id, name, and department
CREATE TABLE staff (
    staff_id INT,
    name VARCHAR(50),
    department VARCHAR(50)
);

-- Insert a new row into the staff table, using the next value from the staff_id_seq sequence for the staff_id column
INSERT INTO staff (staff_id, name, department)
VALUES (NEXTVAL(staff_id_seq), 'John Doe', 'HR');

-- Insert another row into the staff table, using the next value from the staff_id_seq sequence for the staff_id column
INSERT INTO staff (staff_id, name, department)
VALUES (NEXTVAL(staff_id_seq), 'Jane Smith', 'Finance');

SELECT * FROM staff;

┌───────────────────────────────────────────────────────┐
│     staff_id    │       name       │    department    │
├─────────────────┼──────────────────┼──────────────────┤
│               2 │ Jane Smith       │ Finance          │
│               1 │ John Doe         │ HR               │
└───────────────────────────────────────────────────────┘
```
