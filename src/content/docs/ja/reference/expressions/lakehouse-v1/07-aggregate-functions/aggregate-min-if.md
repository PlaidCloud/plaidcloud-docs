---
title: MIN_IF (Lakehouse v1)
description: MIN_IF — 接尾辞 _IF は、任意の集計関数の名前に付加できます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-min-if.md
---

接尾辞 `_IF` は、任意の集計関数の名前に付加できます。この場合、集計関数は追加の引数として条件を受け取ります。

## Analyzeの構文

```python
func.min_if(<column>, <cond>)
```

## Analyzeの例

```python
func.min_if(table.budget, table.departing=='IT').alias('min_it_budget')

| min_it_budget |
|---------------|
|     2000      |
```

## SQLの構文

```sql
MIN_IF(<column>, <cond>)
```

## SQLの例

**テーブルの作成とサンプルデータの挿入**
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

**クエリのデモ: IT 部門の最小予算を求める**

```sql
SELECT MIN_IF(budget, department = 'IT') AS min_it_budget
FROM project_budgets;
```

**結果**
```sql
| min_it_budget |
|---------------|
|     2000      |
```
