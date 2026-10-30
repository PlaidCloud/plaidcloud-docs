---
title: ARG_MIN (Lakehouse v1)
description: ARG_MIN — oblicza wartość arg dla minimalnej wartości val.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-arg-min.md
---

Oblicza wartość `arg` dla minimalnej wartości `val`. Jeśli dla minimalnych wartości `val` istnieje kilka różnych wartości `arg`, zwraca pierwszą z napotkanych.

## Składnia Analyze

```python
func.arg_min(<expr>)
```

## Przykłady Analyze

```python
func.arg_min(table.name, table.score).alias('student_name')

| student_name |
|--------------|
| Charlie      |
```

## Składnia SQL

```sql
ARG_MIN(<arg>, <val>)
```

## Argumenty

| Argumenty | Opis                                                                                              |
|-----------|---------------------------------------------------------------------------------------------------|
| `<arg>`   | Argument dowolnego typu danych obsługiwanego przez PlaidCloud Lakehouse |
| `<val>`   | Wartość dowolnego typu danych obsługiwanego przez PlaidCloud Lakehouse  |

## Typ zwracany

Wartość `arg` odpowiadająca minimalnej wartości `val`.

 odpowiada typowi `arg`.

## Przykłady SQL

Utwórzmy tabelę students z kolumnami id, name i score i wstawmy do niej dane:
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

Teraz możemy użyć funkcji ARG_MIN, aby znaleźć imię ucznia o najniższym wyniku:
```sql
SELECT ARG_MIN(name, score) AS student_name
FROM students;
```

Wynik:
```sql
| student_name |
|--------------|
| Charlie      |
```
