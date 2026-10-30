---
title: SUM_IF (Lakehouse v1)
description: SUM_IF — o sufixo -If pode ser acrescentado ao nome de qualquer função de agregação.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-sum-if.md
---

O sufixo -If pode ser acrescentado ao nome de qualquer função de agregação. Nesse caso, a função de agregação aceita um argumento extra: uma condição.

## Sintaxe do Analyze

```python
func.sum_if(<column>, <cond>)
```

## Exemplos do Analyze

```python
func.sum_if(table.amount, table.status=='Completed').alias('total_amount_completed')

| total_amount_completed |
|------------------------|
|         270.0          |
```

## Sintaxe SQL

```sql
SUM_IF(<column>, <cond>)
```

## Exemplos de SQL

**Criar uma tabela e inserir dados de exemplo**
```sql
CREATE TABLE order_data (
  id INT,
  customer_id INT,
  amount FLOAT,
  status VARCHAR
);

INSERT INTO order_data (id, customer_id, amount, status)
VALUES (1, 1, 100, 'Completed'),
       (2, 2, 50, 'Completed'),
       (3, 3, 80, 'Cancelled'),
       (4, 4, 120, 'Completed'),
       (5, 5, 75, 'Cancelled');
```

**Demonstração de consulta: calcular o valor total dos pedidos concluídos**
```sql
SELECT SUM_IF(amount, status = 'Completed') AS total_amount_completed
FROM order_data;
```

**Resultado**
```sql
| total_amount_completed |
|------------------------|
|         270.0          |
```
