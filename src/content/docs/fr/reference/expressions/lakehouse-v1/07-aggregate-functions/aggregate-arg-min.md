---
title: ARG_MIN (Lakehouse v1)
description: "ARG_MIN : calcule la valeur arg correspondant à la valeur val minimale."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-arg-min.md
---

Calcule la valeur `arg` correspondant à la valeur `val` minimale. Si plusieurs valeurs différentes de `arg` correspondent aux valeurs minimales de `val`, renvoie la première de ces valeurs rencontrée.

## Syntaxe Analyze

```python
func.arg_min(<expr>)
```

## Exemples Analyze

```python
func.arg_min(table.name, table.score).alias('student_name')

| student_name |
|--------------|
| Charlie      |
```

## Syntaxe SQL

```sql
ARG_MIN(<arg>, <val>)
```

## Arguments

| Arguments | Description                                                                                       |
|-----------|---------------------------------------------------------------------------------------------------|
| `<arg>`   | Argument de n'importe quel type de données pris en charge par PlaidCloud Lakehouse |
| `<val>`   | Valeur de n'importe quel type de données pris en charge par PlaidCloud Lakehouse    |

## Type de retour

Valeur `arg` correspondant à la valeur `val` minimale.

 correspond au type de `arg`.

## Exemples SQL

Créons une table students avec les colonnes id, name et score, et insérons-y des données :
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

Nous pouvons maintenant utiliser ARG_MIN pour trouver le nom de l'étudiant ayant la note la plus basse :
```sql
SELECT ARG_MIN(name, score) AS student_name
FROM students;
```

Résultat :
```sql
| student_name |
|--------------|
| Charlie      |
```
