---
title: RETENTION (Lakehouse v1)
description: RETENTION — função de agregação.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-retention.md
---

Função de agregação

A função RETENTION() recebe como argumentos um conjunto de 1 a 32 condições do tipo UInt8 que indicam se uma determinada condição foi cumprida para o evento.

Qualquer condição pode ser especificada como argumento (como em WHERE).

As condições, exceto a primeira, aplicam-se aos pares: o resultado da segunda será verdadeiro se a primeira e a segunda forem verdadeiras, o da terceira se a primeira e a terceira forem verdadeiras, e assim sucessivamente.

## Sintaxe do Analyze

```python
func.retention(<cond1> , <cond2> , ..., <cond32>)
```

## Exemplos do Analyze

```python
table.user_id, func.retention(table.event_type=='signup', table.event_type='login', table.event_type='purchase').alias('sales_amounts')

| user_id | retention |
|---------|-----------|
|   1     | [1, 1, 0] |
|   2     | [1, 0, 1] |
|   3     | [1, 1, 0] |
```

## Sintaxe SQL

```sql
RETENTION( <cond1> , <cond2> , ..., <cond32> );
```

## Argumentos

| Argumentos | Descrição                                   |
|-----------|---------------------------------------------|
| `<cond>`  | Uma expressão que devolve um resultado booleano |

## Tipo de retorno

A matriz de 1 ou 0.

## Exemplos de SQL

**Criar uma tabela e inserir dados de exemplo**
```sql
CREATE TABLE user_events (
  id INT,
  user_id INT,
  event_date DATE,
  event_type VARCHAR
);

INSERT INTO user_events (id, user_id, event_date, event_type)
VALUES (1, 1, '2022-01-01', 'signup'),
       (2, 1, '2022-01-02', 'login'),
       (3, 2, '2022-01-01', 'signup'),
       (4, 2, '2022-01-03', 'purchase'),
       (5, 3, '2022-01-01', 'signup'),
       (6, 3, '2022-01-02', 'login');
```

**Exemplo de consulta: calcular a retenção de utilizadores com base nos eventos de inscrição, início de sessão e compra**
```sql
SELECT
  user_id,
  RETENTION(event_type = 'signup', event_type = 'login', event_type = 'purchase') AS retention
FROM user_events
GROUP BY user_id;
```

**Resultado**
```sql
| user_id | retention |
|---------|-----------|
|   1     | [1, 1, 0] |
|   2     | [1, 0, 1] |
|   3     | [1, 1, 0] |
```
