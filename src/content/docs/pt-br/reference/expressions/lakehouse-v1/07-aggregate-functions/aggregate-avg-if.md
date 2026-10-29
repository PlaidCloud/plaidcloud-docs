---
title: AVG_IF (Lakehouse v1)
description: AVG_IF — o sufixo -If pode ser acrescentado ao nome de qualquer função de agregação.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-avg-if.md
---

O sufixo -If pode ser acrescentado ao nome de qualquer função de agregação. Nesse caso, a função de agregação aceita um argumento extra: uma condição.

## Sintaxe do Analyze

```python
func.avg_if(<column>, <cond>)
```

## Exemplos do Analyze

```python
func.avg_if(table.salary, table.department=='IT').alias('avg_salary_it')

| avg_salary_it   |
|-----------------|
|     65000.0     |
```

## Sintaxe SQL
```sql
AVG_IF(<column>, <cond>)
```

## Exemplos de SQL

**Criar uma tabela e inserir dados de exemplo**
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

**Demonstração de consulta: calcular o salário médio do departamento de TI**

```sql
SELECT AVG_IF(salary, department = 'IT') AS avg_salary_it
FROM employees;
```

**Resultado**
```sql
| avg_salary_it   |
|-----------------|
|     65000.0     |
```
