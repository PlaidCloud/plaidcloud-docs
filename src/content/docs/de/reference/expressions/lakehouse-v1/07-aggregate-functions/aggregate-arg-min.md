---
title: ARG_MIN (Lakehouse v1)
description: ARG_MIN – berechnet den arg-Wert zum kleinsten val-Wert.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-arg-min.md
---

Berechnet den `arg`-Wert zum kleinsten `val`-Wert. Wenn es mehrere verschiedene `arg`-Werte für die kleinsten `val`-Werte gibt, wird der erste dieser gefundenen Werte zurückgegeben.

## Analyze-Syntax

```python
func.arg_min(<expr>)
```

## Analyze-Beispiele

```python
func.arg_min(table.name, table.score).alias('student_name')

| student_name |
|--------------|
| Charlie      |
```

## SQL-Syntax

```sql
ARG_MIN(<arg>, <val>)
```

## Argumente

| Argumente | Beschreibung                                                                                      |
|-----------|---------------------------------------------------------------------------------------------------|
| `<arg>`   | Argument eines beliebigen Datentyps, den PlaidCloud Lakehouse unterstützt |
| `<val>`   | Wert eines beliebigen Datentyps, den PlaidCloud Lakehouse unterstützt     |

## Rückgabetyp

`arg`-Wert, der dem kleinsten `val`-Wert entspricht.

 entspricht dem `arg`-Typ.

## SQL-Beispiele

Erstellen wir eine Tabelle students mit den Spalten id, name und score und fügen einige Daten ein:
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

Nun können wir mit ARG_MIN den Namen des Studierenden mit der niedrigsten Punktzahl ermitteln:
```sql
SELECT ARG_MIN(name, score) AS student_name
FROM students;
```

Ergebnis:
```sql
| student_name |
|--------------|
| Charlie      |
```
