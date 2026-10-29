---
title: MAX_IF (Lakehouse v1)
description: MAX_IF — o sufixo _IF pode ser acrescentado ao nome de qualquer função de agregação.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-max-if.md
---

O sufixo `_IF` pode ser acrescentado ao nome de qualquer função de agregação. Neste caso, a função de agregação aceita um argumento adicional – uma condição.

## Sintaxe do Analyze

```python
func.max_if(<column>, <cond>)
```

## Exemplos do Analyze

```python
func.max_if(table.revenue, table.salesperson_id==1).alias('max_revenue_salesperson_1')

| max_revenue_salesperson_1 |
|---------------------------|
|           3000            |
```

## Exemplo de SQL

```sql
MAX_IF(<column>, <cond>)
```

## Exemplos de SQL

**Criar uma tabela e inserir dados de exemplo**
```sql
CREATE TABLE sales (
  id INT,
  salesperson_id INT,
  product_id INT,
  revenue FLOAT
);

INSERT INTO sales (id, salesperson_id, product_id, revenue)
VALUES (1, 1, 1, 1000),
       (2, 1, 2, 2000),
       (3, 1, 3, 3000),
       (4, 2, 1, 1500),
       (5, 2, 2, 2500);
```

**Exemplo de consulta: encontrar a receita máxima do vendedor com o ID 1**

```sql
SELECT MAX_IF(revenue, salesperson_id = 1) AS max_revenue_salesperson_1
FROM sales;
```

**Resultado**
```sql
| max_revenue_salesperson_1 |
|---------------------------|
|           3000            |
```
