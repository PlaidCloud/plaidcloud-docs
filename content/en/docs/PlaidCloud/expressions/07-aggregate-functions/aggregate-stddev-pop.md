---
title: STDDEV_POP
title_includes: STD, STDDEV
---

Aggregate function.

The STDDEV_POP() function returns the population standard deviation(the square root of VAR_POP()) of an expression.

{{< note >}}
STD() or STDDEV() can also be used, which are equivalent but not standard SQL.
{{< /note >}}

{{< caution >}}
NULL values are not counted.
{{< /caution >}}

## Analyze Syntax

```python
func.stddev_pop(<expr>)
```

## Analyze Examples
```python
func.stddev_pop(table.score).alias('test_score_stddev_pop')

| test_score_stddev_pop |
|-----------------------|
|        7.07107        |
```

## SQL Syntax

```sql
STDDEV_POP(<expr>)
STDDEV(<expr>)
STD(<expr>)
```

## Arguments

| Arguments | Description              |
|-----------|--------------------------|
| `<expr>`  | Any numerical expression |

## Return Type

double

## SQL Examples

**Create a Table and Insert Sample Data**
```sql
CREATE TABLE test_scores (
  id INT,
  student_id INT,
  score FLOAT
);

INSERT INTO test_scores (id, student_id, score)
VALUES (1, 1, 80),
       (2, 2, 85),
       (3, 3, 90),
       (4, 4, 95),
       (5, 5, 100);
```

**Query Demo: Calculate Population Standard Deviation of Test Scores**
```sql
SELECT STDDEV_POP(score) AS test_score_stddev_pop
FROM test_scores;
```

**Result**
```sql
| test_score_stddev_pop |
|-----------------------|
|        7.07107        |
```