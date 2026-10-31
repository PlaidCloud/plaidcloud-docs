---
title: TO_UNIX_TIMESTAMP (Lakehouse v1)
description: TO_UNIX_TIMESTAMP — converte um timestamp num formato de data/hora para o formato de timestamp Unix.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-unix-timestamp.md
---

Converte um timestamp num formato de data/hora para o formato de timestamp Unix. Um timestamp Unix representa o número de segundos decorridos desde 1 de janeiro de 1970, às 00:00:00 UTC.

## Sintaxe do Analyze

```python
func.to_unix_timestamp(<expr>)
```

## Exemplos do Analyze

```python
func.to_unix_timestamp('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_unix_timestamp('2023-11-12 09:38:18.165575')           │
│                          UInt32                                │
├────────────────────────────────────────────────────────────────┤
│                                                     1699781898 │
└────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_UNIX_TIMESTAMP(<expr>)
```

## Argumentos

| Argumentos  | Descrição           |
| ----------- | ------------------- |
| `<expr>`    | Timestamp           |

Para mais informações sobre o tipo de dados timestamp, veja Date & Time.

## Tipo de Retorno

`BIGINT`

## Exemplos SQL

```sql
SELECT
  to_unix_timestamp('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────────────┐
│ to_unix_timestamp('2023-11-12 09:38:18.165575') │
│                      UInt32                     │
├─────────────────────────────────────────────────┤
│                                      1699781898 │
└─────────────────────────────────────────────────┘
```
