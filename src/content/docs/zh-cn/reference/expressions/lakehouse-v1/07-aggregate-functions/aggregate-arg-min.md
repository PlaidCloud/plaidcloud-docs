---
title: ARG_MIN (Lakehouse v1)
description: ARG_MIN：计算最小 val 值所对应的 arg 值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-arg-min.md
---

计算最小 `val` 值所对应的 `arg` 值。如果最小 `val` 值对应多个不同的 `arg` 值，则返回遇到的第一个值。

## Analyze 语法

```python
func.arg_min(<expr>)
```

## Analyze 示例

```python
func.arg_min(table.name, table.score).alias('student_name')

| student_name |
|--------------|
| Charlie      |
```

## SQL 语法

```sql
ARG_MIN(<arg>, <val>)
```

## 参数

| 参数 | 说明 |
|-----------|---------------------------------------------------------------------------------------------------|
| `<arg>`   | PlaidCloud Lakehouse 支持的任意数据类型的参数 |
| `<val>`   | PlaidCloud Lakehouse 支持的任意数据类型的值 |

## 返回类型

与最小 `val` 值对应的 `arg` 值。

 与 `arg` 的类型一致。

## SQL 示例

创建一个包含 id、name 和 score 列的 students 表，并插入一些数据：
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

现在可以使用 ARG_MIN 查找得分最低的学生姓名：
```sql
SELECT ARG_MIN(name, score) AS student_name
FROM students;
```

结果：
```sql
| student_name |
|--------------|
| Charlie      |
```
