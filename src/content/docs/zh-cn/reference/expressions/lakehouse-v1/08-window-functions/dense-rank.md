---
title: DENSE_RANK (Lakehouse v1)
description: DENSE_RANK：返回某个值在一组值中的排名，排名之间没有间隔。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/08-window-functions/dense-rank.md
---

返回某个值在一组值中的排名，排名之间没有间隔。

排名值从 1 开始，依次递增。

如果两个值相同，则它们的排名相同。

## Analyze 语法

```python
func.dense_rank().over(partition_by=[<columns>], order_by=[<columns>])
```

## Analyze 示例

```python
table.department, func.sum(salary), func.dense_rank().over(order_by=func.sum(table.salary).desc()).alias('dense_rank')

| department | total_salary | dense_rank |
|------------|--------------|------------|
| IT         | 172000       | 1          |
| HR         | 160000       | 2          |
| Sales      | 77000        | 3          |
```

## SQL 语法

```sql
DENSE_RANK() OVER ( [ PARTITION BY <expr1> ] ORDER BY <expr2> [ ASC | DESC ] [ <window_frame> ] )
```

## SQL 示例

**创建表**
```sql
CREATE TABLE employees (
  employee_id INT,
  first_name VARCHAR,
  last_name VARCHAR,
  department VARCHAR,
  salary INT
);
```

**插入数据**
```sql
INSERT INTO employees (employee_id, first_name, last_name, department, salary) VALUES
  (1, 'John', 'Doe', 'IT', 90000),
  (2, 'Jane', 'Smith', 'HR', 85000),
  (3, 'Mike', 'Johnson', 'IT', 82000),
  (4, 'Sara', 'Williams', 'Sales', 77000),
  (5, 'Tom', 'Brown', 'HR', 75000);
```

**使用 DENSE_RANK 计算各部门的薪资总额**

```sql
SELECT
    department,
    SUM(salary) AS total_salary,
    DENSE_RANK() OVER (ORDER BY SUM(salary) DESC) AS dense_rank
FROM
    employees
GROUP BY
    department;
```

结果：

| department | total_salary | dense_rank |
|------------|--------------|------------|
| IT         | 172000       | 1          |
| HR         | 160000       | 2          |
| Sales      | 77000        | 3          |
