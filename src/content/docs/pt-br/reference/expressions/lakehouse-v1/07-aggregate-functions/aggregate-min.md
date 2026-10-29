---
title: MIN (Lakehouse v1)
description: MIN — retorna o valor mínimo em um conjunto de valores.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-min.md
---

Função de agregação.

A função MIN() retorna o valor mínimo em um conjunto de valores.

## Sintaxe do Analyze

```python
func.min(<column>)
```

## Exemplos do Analyze

```python
table.station_id, func.min(table.price).alias('min_price')

| station_id | min_price |
|------------|-----------|
|     1      |   3.45    |
```

## Sintaxe SQL

```sql
MIN(<expr>)
```

## Argumentos

| Argumentos | Descrição        |
|-----------|------------------|
| `<expr>`  | Qualquer expressão |

## Tipo de retorno

O valor mínimo, no tipo do valor.

## Exemplos de SQL

---
title: MIN
---

Função de agregação.

A função MIN() retorna o valor mínimo em um conjunto de valores.

## Sintaxe SQL

```sql
MIN(expression)
```

## Argumentos

| Argumentos  | Descrição   |
| ----------- | ----------- |
| expression  | Qualquer expressão |

## Tipo de retorno

O valor mínimo, no tipo do valor.

## Exemplos de SQL

**Criar uma tabela e inserir dados de exemplo**
```sql
CREATE TABLE gas_prices (
  id INT,
  station_id INT,
  price FLOAT
);

INSERT INTO gas_prices (id, station_id, price)
VALUES (1, 1, 3.50),
       (2, 1, 3.45),
       (3, 1, 3.55),
       (4, 2, 3.40),
       (5, 2, 3.35);
```

**Demonstração de consulta: encontrar o preço mínimo da gasolina no posto 1**
```sql
SELECT station_id, MIN(price) AS min_price
FROM gas_prices
WHERE station_id = 1
GROUP BY station_id;
```

**Resultado**
```sql
| station_id | min_price |
|------------|-----------|
|     1      |   3.45    |
```
