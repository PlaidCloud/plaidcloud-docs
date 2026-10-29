---
title: ARG_MAX (Lakehouse v1)
description: ARG_MAX — calcula o valor de arg correspondente ao valor máximo de val.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-arg-max.md
---

Calcula o valor de `arg` correspondente ao valor máximo de `val`. Se houver vários valores de `arg` para os valores máximos de `val`, retorna o primeiro desses valores encontrado.

## Sintaxe do Analyze

```python
func.arg_max(<expr>)
```

## Exemplos do Analyze

```python
func.arg_max(table.product, table.price).alias('max_price_product')

| max_price_product |
| ----------------- |
| Product C         |
```

## Sintaxe SQL

```sql
ARG_MAX(<arg>, <val>)
```

## Argumentos

| Argumentos | Descrição                                                                                         |
|-----------|---------------------------------------------------------------------------------------------------|
| `<arg>`   | Argumento de qualquer tipo de dados com suporte do PlaidCloud Lakehouse |
| `<val>`   | Valor de qualquer tipo de dados com suporte do PlaidCloud Lakehouse     |

## Tipo de retorno

Valor de `arg` que corresponde ao valor máximo de `val`.

 corresponde ao tipo de `arg`.

## Exemplos de SQL

**Criar uma tabela e inserir dados de exemplo**

Vamos criar uma tabela chamada "sales" e inserir alguns dados de exemplo:
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

**Consulta: usar a função ARG_MAX()**

Agora, vamos usar a função ARG_MAX() para encontrar o produto com o preço máximo:
```sql
SELECT ARG_MAX(product, price) AS max_price_product
FROM sales;
```

O resultado deve ser semelhante a este:
```sql
| max_price_product |
| ----------------- |
| Product C         |
```
