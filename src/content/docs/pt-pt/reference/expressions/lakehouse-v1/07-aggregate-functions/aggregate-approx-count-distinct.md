---
title: APPROX_COUNT_DISTINCT (Lakehouse v1)
description: APPROX_COUNT_DISTINCT — estima o número de valores distintos num conjunto de dados com o algoritmo HyperLogLog.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-approx-count-distinct.md
---

Estima o número de valores distintos num conjunto de dados com o algoritmo [HyperLogLog](https://en.wikipedia.org/wiki/HyperLogLog). 

O algoritmo HyperLogLog fornece uma aproximação do número de elementos únicos com pouca memória e tempo. Considere utilizar esta função com conjuntos de dados de grande dimensão em que seja aceitável um resultado estimado. Em troca de alguma precisão, este é um método rápido e eficiente de devolver contagens distintas.

Para obter um resultado exato, utilize [COUNT_DISTINCT](../aggregate-count-distinct). Consulte os [Exemplos](#exemplos-de-sql) para obter mais explicações.

## Sintaxe do Analyze

```python
func.approx_count_distinct(<expr>)
```

## Exemplos do Analyze

```python
func.approx_count_distinct(table.user_id).alias('approx_distinct_user_count')

| approx_distinct_user_count |
|----------------------------|
|             4              |
```

## Sintaxe SQL

```sql
APPROX_COUNT_DISTINCT(<expr>)
```

## Tipo de retorno

Inteiro.

## Exemplos de SQL

**Criar uma tabela e inserir dados de exemplo**
```sql
CREATE TABLE user_events (
  id INT,
  user_id INT,
  event_name VARCHAR
);

INSERT INTO user_events (id, user_id, event_name)
VALUES (1, 1, 'Login'),
       (2, 2, 'Login'),
       (3, 3, 'Login'),
       (4, 1, 'Logout'),
       (5, 2, 'Logout'),
       (6, 4, 'Login'),
       (7, 1, 'Login');
```

**Exemplo de consulta: estimar o número de IDs de utilizador distintos**
```sql
SELECT APPROX_COUNT_DISTINCT(user_id) AS approx_distinct_user_count
FROM user_events;
```

**Resultado**
```sql
| approx_distinct_user_count |
|----------------------------|
|             4              |
```
