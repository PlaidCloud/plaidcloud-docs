---
title: MIN_IF (Lakehouse v1)
description: MIN_IF — o sufixo _IF pode ser acrescentado ao nome de qualquer função de agregação.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-min-if.md
---

O sufixo `_IF` pode ser acrescentado ao nome de qualquer função de agregação. Neste caso, a função de agregação aceita um argumento adicional – uma condição.

## Sintaxe do Analyze

```python
func.min_if(<column>, <cond>)
```

## Exemplos do Analyze

```python
func.min_if(table.budget, table.departing=='IT').alias('min_it_budget')

| min_it_budget |
|---------------|
|     2000      |
```

## Sintaxe SQL

```sql
MIN_IF(<column>, <cond>)
```

## Exemplos de SQL

**Criar uma tabela e inserir dados de exemplo**
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

**Exemplo de consulta: encontrar o orçamento mínimo do departamento de TI**

```sql
SELECT MIN_IF(budget, department = 'IT') AS min_it_budget
FROM project_budgets;
```

**Resultado**
```sql
| min_it_budget |
|---------------|
|     2000      |
```
