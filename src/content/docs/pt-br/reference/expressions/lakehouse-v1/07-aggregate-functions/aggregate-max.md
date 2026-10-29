---
title: MAX (Lakehouse v1)
description: MAX — retorna o valor máximo em um conjunto de valores.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-max.md
---

Função de agregação.

A função MAX() retorna o valor máximo em um conjunto de valores.

## Sintaxe do Analyze

```python
func.max(<column>)
```

## Exemplos do Analyze

```python
table.city, func.max(table.temperature).alias('max_temperature')

|    city    | max_temperature |
|------------|-----------------|
| New York   |       32        |
```

## Sintaxe SQL

```sql
MAX(<expr>)
```

## Argumentos

| Argumentos | Descrição |
|-----------| ----------- |
| `<expr>`  | Qualquer expressão |

## Tipo de retorno

O valor máximo, no tipo do valor.

## Exemplos de SQL

**Criar uma tabela e inserir dados de exemplo**
```sql
CREATE TABLE temperatures (
  id INT,
  city VARCHAR,
  temperature FLOAT
);

INSERT INTO temperatures (id, city, temperature)
VALUES (1, 'New York', 30),
       (2, 'New York', 28),
       (3, 'New York', 32),
       (4, 'Los Angeles', 25),
       (5, 'Los Angeles', 27);
```

**Demonstração de consulta: encontrar a temperatura máxima da cidade de Nova York**

```sql
SELECT city, MAX(temperature) AS max_temperature
FROM temperatures
WHERE city = 'New York'
GROUP BY city;
```

**Resultado**
```sql
|    city    | max_temperature |
|------------|-----------------|
| New York   |       32        |
```
