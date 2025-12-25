---
title: COUNT
---

The COUNT() function returns the number of records returned by a SELECT query.

{{< caution >}}
NULL values are not counted.
{{< /caution >}}

## Analyze Syntax

```python
func.count(<column>)
```

## Analyze Examples
```python
func.count(table.grade).alias('count_valid_grades')

| count_valid_grades |
|--------------------|
|          4         |
```

## SQL Syntax

```sql
COUNT(<expr>)
```

## Arguments

| Arguments | Description                                                                                                                                                     |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<expr>`  | Any expression. <br /> This may be a column name, the result of another function, or a math operation.<br />`*` is also allowed, to indicate pure row counting. |

## Return Type

An integer.

## SQL Examples

**Create a Table and Insert Sample Data**
```sql
CREATE TABLE students (
  id INT,
  name VARCHAR,
  age INT,
  grade FLOAT NULL
);

INSERT INTO students (id, name, age, grade)
VALUES (1, 'John', 21, 85),
       (2, 'Emma', 22, NULL),
       (3, 'Alice', 23, 90),
       (4, 'Michael', 21, 88),
       (5, 'Sophie', 22, 92);

```

**Query Demo: Count Students with Valid Grades**
```sql
SELECT COUNT(grade) AS count_valid_grades
FROM students;
```

**Result**
```sql
| count_valid_grades |
|--------------------|
|          4         |
```