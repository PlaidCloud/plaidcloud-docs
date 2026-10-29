---
title: ANY (Lakehouse v1)
description: ANY — devolve o primeiro valor não NULL encontrado num conjunto; o resultado é indeterminado quando a ordem de execução varia.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-any.md
---

Função de agregação.

A função ANY() seleciona o primeiro valor encontrado (não NULL), a menos que todas as linhas tenham valores NULL nessa coluna. A consulta pode ser executada em qualquer ordem e até numa ordem diferente de cada vez, pelo que o resultado desta função é indeterminado. Para obter um resultado determinado, pode utilizar a função ‘min’ ou ‘max’ em vez de ‘any’.

## Sintaxe do Analyze

```python
func.any(<expr>)
```

## Exemplos do Analyze

```python
func.any(table.product_name).alias('any_product_name')

| any_product_name |
|------------------|
| Laptop           |
```

## Sintaxe SQL

```sql
ANY(<expr>)
```

## Argumentos

| Argumentos | Descrição      |
|-----------|----------------|
| `<expr>`  | Qualquer expressão |

## Tipo de retorno

O primeiro valor encontrado (não NULL), no tipo do valor. Se todos os valores forem NULL, o valor devolvido é NULL.

## Exemplos de SQL

**Criar uma tabela e inserir dados de exemplo**
```sql
CREATE TABLE product_data (
  id INT,
  product_name VARCHAR NULL,
  price FLOAT NULL
);

INSERT INTO product_data (id, product_name, price)
VALUES (1, 'Laptop', 1000),
       (2, NULL, 800),
       (3, 'Keyboard', NULL),
       (4, 'Mouse', 25),
       (5, 'Monitor', 150);
```

**Exemplo de consulta: obter o primeiro nome de produto não NULL encontrado**
```sql
SELECT ANY(product_name) AS any_product_name
FROM product_data;
```

**Resultado**
```sql
| any_product_name |
|------------------|
| Laptop           |
```
