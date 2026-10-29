---
title: AVG_IF (Lakehouse v1)
description: AVG_IF — 接尾辞 -If は、任意の集計関数の名前に付加できます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-avg-if.md
---

接尾辞 -If は、任意の集計関数の名前に付加できます。この場合、集計関数は追加の引数として条件を受け取ります。

## Analyzeの構文

```python
func.avg_if(<column>, <cond>)
```

## Analyzeの例

```python
func.avg_if(table.salary, table.department=='IT').alias('avg_salary_it')

| avg_salary_it   |
|-----------------|
|     65000.0     |
```

## SQLの構文
```sql
AVG_IF(<column>, <cond>)
```

## SQLの例

**テーブルの作成とサンプルデータの挿入**
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

**クエリのデモ: IT 部門の平均給与を計算する**

```sql
SELECT AVG_IF(salary, department = 'IT') AS avg_salary_it
FROM employees;
```

**結果**
```sql
| avg_salary_it   |
|-----------------|
|     65000.0     |
```
