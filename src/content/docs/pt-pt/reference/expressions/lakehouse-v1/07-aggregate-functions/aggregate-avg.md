---
title: AVG (Lakehouse v1)
description: AVG — devolve o valor médio de uma expressão, ignorando os valores NULL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-avg.md
---

Função de agregação.

A função AVG() devolve o valor médio de uma expressão.

**Nota:** os valores NULL não são contados.


## Sintaxe do Analyze

```python
func.avg(<column>)
```

## Exemplos do Analyze

```python
func.avg(table.price).alias('avg_price')

| avg_price |
| --------- |
| 20.4      |
```

## Sintaxe SQL

```sql
AVG(<expr>)
```

## Argumentos

| Argumentos | Descrição                |
|-----------|--------------------------|
| `<expr>`  | Qualquer expressão numérica |

## Tipo de retorno

double

## Exemplos de SQL

**Criar uma tabela e inserir dados de exemplo**

Vamos criar uma tabela com o nome "sales" e inserir alguns dados de exemplo:
```sql
CREATE TABLE sales (
  id INTEGER,
  product VARCHAR(50),
  price FLOAT
);

INSERT INTO sales (id, product, price)
VALUES (1, 'Product A', 10.5),
       (2, 'Product B', 20.75),
       (3, 'Product C', 30.0),
       (4, 'Product D', 15.25),
       (5, 'Product E', 25.5);
```

**Consulta: utilizar a função AVG()**

Agora, vamos utilizar a função AVG() para encontrar o preço médio de todos os produtos da tabela "sales":
```sql
SELECT AVG(price) AS avg_price
FROM sales;
```

O resultado deverá ser o seguinte:
```sql
| avg_price |
| --------- |
| 20.4      |
```
