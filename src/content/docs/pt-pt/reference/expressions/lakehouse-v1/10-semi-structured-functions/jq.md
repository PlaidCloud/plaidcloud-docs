---
title: JQ (Lakehouse v1)
description: JQ — a função JQ é uma função SQL que devolve conjuntos e permite aplicar jq.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/jq.md
---

A função JQ é uma função SQL que devolve conjuntos e permite aplicar filtros [jq](https://jqlang.github.io/jq/) a dados JSON armazenados em colunas Variant. Com esta função, pode processar dados JSON aplicando um filtro jq especificado e obter os resultados como um conjunto de linhas.

## Sintaxe SQL

```sql
JQ (<jq_expression>, <json_data>)
```

| Parâmetro       | Descrição                                                                                                                                                                                                                                                                                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `jq_expression` | Uma expressão de filtro `jq` que define como processar e transformar dados JSON através da sintaxe `jq`. Esta expressão pode especificar como selecionar, modificar e manipular dados dentro de objetos e matrizes JSON. Para obter informações sobre a sintaxe, os filtros e as funções suportados pelo jq, consulte o [Manual do jq](https://jqlang.github.io/jq/manual/#basic-filters). |
| `json_data`     | A entrada em formato JSON que pretende processar ou transformar com a expressão de filtro `jq`. Pode ser um objeto JSON, uma matriz ou qualquer estrutura de dados JSON válida.                                                                                                                                                                             |

## Tipo de retorno

A função JQ devolve um conjunto de valores JSON, em que cada valor corresponde a um elemento do resultado transformado ou extraído com base em `<jq_expression>`.

## Exemplos de SQL

Para começar, criamos uma tabela com o nome `customer_data` com as colunas `id` e `profile`, em que `profile` é do tipo JSON para armazenar informações do utilizador:

```sql
CREATE TABLE customer_data (
    id INT,
    profile JSON
);

INSERT INTO customer_data VALUES
    (1, '{"name": "Alice", "age": 30, "city": "New York"}'),
    (2, '{"name": "Bob", "age": 25, "city": "Los Angeles"}'),
    (3, '{"name": "Charlie", "age": 35, "city": "Chicago"}');
```

Este exemplo extrai campos específicos dos dados JSON:

```sql
SELECT
    id,
    jq('.name', profile) AS customer_name
FROM
    customer_data;

┌─────────────────────────────────────┐
│        id       │   customer_name   │
├─────────────────┼───────────────────┤
│               1 │ "Alice"           │
│               2 │ "Bob"             │
│               3 │ "Charlie"         │
└─────────────────────────────────────┘
```

Este exemplo seleciona o ID do utilizador e a idade incrementada em 1 para cada utilizador:

```sql
SELECT
    id,
    jq('.age + 1', profile) AS updated_age
FROM
    customer_data;

┌─────────────────────────────────────┐
│        id       │    updated_age    │
├─────────────────┼───────────────────┤
│               1 │ 31                │
│               2 │ 26                │
│               3 │ 36                │
└─────────────────────────────────────┘
```

Este exemplo converte os nomes das cidades para maiúsculas:

```sql
SELECT
    id,
    jq('.city | ascii_upcase', profile) AS city_uppercase
FROM
    customer_data;

┌─────────────────────────────────────┐
│        id       │   city_uppercase  │
├─────────────────┼───────────────────┤
│               1 │ "NEW YORK"        │
│               2 │ "LOS ANGELES"     │
│               3 │ "CHICAGO"         │
└─────────────────────────────────────┘
```
