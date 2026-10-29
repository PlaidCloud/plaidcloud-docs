---
title: TRY_TO_TIMESTAMP (Lakehouse v1)
description: TRY_TO_TIMESTAMP — uma variante de TO_TIMESTAMP no PlaidCloud Lakehouse que, ao efetuar a mesma conversão, devolve NULL em caso de falha.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/try-to-timestamp.md
---

Uma variante de [TO_TIMESTAMP](../to-timestamp) no PlaidCloud Lakehouse que, embora efetue a mesma conversão de uma expressão de entrada para um timestamp, incorpora suporte para tratamento de erros: devolve NULL se a conversão falhar, em vez de gerar um erro.

Veja também: [TO_TIMESTAMP](../to-timestamp)

## Sintaxe do Analyze

```python
func.try_to_timestamp(<expr>)
```

## Exemplos do Analyze

```python
func.try_to_timestamp('2022-01-02 02:00:11'), func.try_to_datetime('2022-01-02 02:00:11'), func.try_to_timestamp('plaidcloud')
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.try_to_timestamp('2022-01-02 02:00:11') │ func.try_to_datetime('2022-01-02 02:00:11') │ func.try_to_timestamp('plaidcloud') │
│                Timestamp                │                Timestamp                         │                                     │
├─────────────────────────────────────────┼──────────────────────────────────────────────────┤─────────────────────────────────────│
│ 2022-01-02 02:00:11                     │ 2022-01-02 02:00:11                              │ NULL                                │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
-- Convert a string or integer to a timestamp
TRY_TO_TIMESTAMP(<expr>)

-- Convert a string to a timestamp using the given pattern
TRY_TO_TIMESTAMP(<expr, expr>)
```

## Aliases

- [TRY_TO_DATETIME](../try-to-datetime)

## Exemplos SQL

```sql
SELECT TRY_TO_TIMESTAMP('2022-01-02 02:00:11'), TRY_TO_DATETIME('2022-01-02 02:00:11');

┌──────────────────────────────────────────────────────────────────────────────────┐
│ try_to_timestamp('2022-01-02 02:00:11') │ try_to_datetime('2022-01-02 02:00:11') │
│                Timestamp                │                Timestamp               │
├─────────────────────────────────────────┼────────────────────────────────────────┤
│ 2022-01-02 02:00:11                     │ 2022-01-02 02:00:11                    │
└──────────────────────────────────────────────────────────────────────────────────┘

SELECT TRY_TO_TIMESTAMP('databend'), TRY_TO_DATETIME('databend');

┌────────────────────────────────────────────────────────────┐
│ try_to_timestamp('databend') │ try_to_datetime('databend') │
├──────────────────────────────┼─────────────────────────────┤
│ NULL                         │ NULL                        │
└────────────────────────────────────────────────────────────┘
```
