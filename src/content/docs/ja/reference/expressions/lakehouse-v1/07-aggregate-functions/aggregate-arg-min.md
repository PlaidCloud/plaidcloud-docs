---
title: ARG_MIN (Lakehouse v1)
description: ARG_MIN — val の最小値に対応する arg の値を計算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-arg-min.md
---

`val` の最小値に対応する `arg` の値を計算します。`val` の最小値に対して `arg` の値が複数ある場合は、最初に見つかった値を返します。

## Analyzeの構文

```python
func.arg_min(<expr>)
```

## Analyzeの例

```python
func.arg_min(table.name, table.score).alias('student_name')

| student_name |
|--------------|
| Charlie      |
```

## SQLの構文

```sql
ARG_MIN(<arg>, <val>)
```

## 引数

| 引数 | 説明 |
|-----------|---------------------------------------------------------------------------------------------------|
| `<arg>`   | PlaidCloud Lakehouse がサポートする任意のデータ型の引数 |
| `<val>`   | PlaidCloud Lakehouse がサポートする任意のデータ型の値 |

## 戻り値の型

`val` の最小値に対応する `arg` の値。

 `arg` の型と一致します。

## SQLの例

id、name、score の列を持つ students テーブルを作成し、データを挿入します。
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

ARG_MIN を使用して、スコアが最も低い学生の名前を求めます。
```sql
SELECT ARG_MIN(name, score) AS student_name
FROM students;
```

結果:
```sql
| student_name |
|--------------|
| Charlie      |
```
