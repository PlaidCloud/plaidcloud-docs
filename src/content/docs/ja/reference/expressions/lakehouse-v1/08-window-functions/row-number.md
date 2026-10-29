---
title: ROW_NUMBER（Lakehouse v1）
description: ROW_NUMBER — 結果のパーティション内の各行に、一時的な連番を割り当てます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/row-number.md
---

結果セットのパーティション内の各行に、一時的な連番を割り当てます。各パーティションの最初の行が1になります。

## Analyze Syntax

```python
func.row_number().over(partition_by=[<columns>], order_by=[<columns>])
```

## Analyze Examples

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

## SQL Syntax

```sql
ROW_NUMBER() 
  OVER ( [ PARTITION BY <expr1> [, <expr2> ... ] ]
  ORDER BY <expr3> [ , <expr4> ... ] [ { ASC | DESC } ] )
```

| パラメーター    | 必須？ | 説明                                                                                                |
|--------------|-----------|------------------------------------------------------------------------------------------------------------|
| ORDER BY     | はい       | 各パーティション内の行の順序を指定します。                                                         |
| ASC / DESC   | いいえ        | 各パーティション内のソート順を指定します。デフォルトはASC（昇順）です。                         |
| QUALIFY      | いいえ        | 条件に基づいて行をフィルターします。                                                                          |

## SQL Examples

この例では、ROW_NUMBER()を使用して、部門ごとに従業員へ給与の降順で連番を割り当てます。

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
