---
title: ARG_MIN (Lakehouse v1)
description: ARG_MIN — calcula o valor de arg correspondente ao valor mínimo de val.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-arg-min.md
---

Calcula o valor de `arg` correspondente ao valor mínimo de `val`. Se existirem vários valores diferentes de `arg` para os valores mínimos de `val`, devolve o primeiro desses valores encontrado.

## Sintaxe do Analyze

```python
func.arg_min(<expr>)
```

## Exemplos do Analyze

```python
func.arg_min(table.name, table.score).alias('student_name')

| student_name |
|--------------|
| Charlie      |
```

## Sintaxe SQL

```sql
ARG_MIN(<arg>, <val>)
```

## Argumentos

| Argumentos | Descrição                                                                                         |
|-----------|---------------------------------------------------------------------------------------------------|
| `<arg>`   | Argumento de qualquer tipo de dados suportado pelo PlaidCloud Lakehouse |
| `<val>`   | Valor de qualquer tipo de dados suportado pelo PlaidCloud Lakehouse     |

## Tipo de retorno

Valor de `arg` correspondente ao valor mínimo de `val`.

 corresponde ao tipo de `arg`.

## Exemplos de SQL

Vamos criar uma tabela students com as colunas id, name e score, e inserir alguns dados:
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

Agora, podemos utilizar ARG_MIN para encontrar o nome do aluno com a pontuação mais baixa:
```sql
SELECT ARG_MIN(name, score) AS student_name
FROM students;
```

Resultado:
```sql
| student_name |
|--------------|
| Charlie      |
```
