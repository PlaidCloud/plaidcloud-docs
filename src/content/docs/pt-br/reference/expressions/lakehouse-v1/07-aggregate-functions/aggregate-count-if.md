---
title: COUNT_IF (Lakehouse v1)
description: COUNT_IF — o sufixo _IF pode ser acrescentado ao nome de qualquer função de agregação.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-count-if.md
---

O sufixo `_IF` pode ser acrescentado ao nome de qualquer função de agregação. Nesse caso, a função de agregação aceita um argumento extra: uma condição.

## Sintaxe do Analyze

```python
func.count_if(<column>, <cond>)
```

## Exemplos do Analyze

```python
func.count_if(table.status, table.status=='Completed').alias('completed_orders')

| completed_orders |
|------------------|
|        3         |
```

## Exemplo de SQL
```sql
COUNT_IF(<column>, <cond>)
```

## Exemplos de SQL

**Criar uma tabela e inserir dados de exemplo**
```sql
CREATE TABLE orders (
  id INT,
  customer_id INT,
  status VARCHAR,
  total FLOAT
);

INSERT INTO orders (id, customer_id, status, total)
VALUES (1, 1, 'completed', 100),
       (2, 2, 'completed', 200),
       (3, 1, 'pending', 150),
       (4, 3, 'completed', 250),
       (5, 2, 'pending', 300);
```

**Demonstração de consulta: contar pedidos concluídos**
```sql
SELECT COUNT_IF(status, status = 'completed') AS completed_orders
FROM orders;
```

**Resultado**
```sql
| completed_orders |
|------------------|
|        3         |
```
