---
title: TIMESTAMP_DIFF (Lakehouse v1)
description: TIMESTAMP_DIFF — calcula a diferença entre dois timestamps e retorna o resultado como um INTERVAL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/timestamp-diff.md
---

Calcula a diferença entre dois timestamps e retorna o resultado como um INTERVAL.

## Sintaxe do Analyze

```python
func.timestamp_diff(<timestamp1>, <timestamp2>)
```

## Exemplos do Analyze

```python
func.timestamp_diff(func.to_timestamp('2025-02-01'), func.to_timestamp('2025-01-01'))
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ func.timestamp_diff(func.to_timestamp('2025-02-01'), func.to_timestamp('2025-01-01'))  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 744:00:00                                                                              │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TIMESTAMP_DIFF(<timestamp1>, <timestamp2>)
```

## Tipo de retorno

INTERVAL (formatado como `hours:minutes:seconds`).

## Exemplos de SQL

Este exemplo mostra que a diferença de tempo entre 1º de fevereiro de 2025 e 1º de janeiro de 2025 é de 744 horas, o que corresponde a 31 dias:

```sql
SELECT TIMESTAMP_DIFF('2025-02-01'::TIMESTAMP, '2025-01-01'::TIMESTAMP);

┌──────────────────────────────────────────────────────────────────┐
│ timestamp_diff('2025-02-01'::TIMESTAMP, '2025-01-01'::TIMESTAMP) │
├──────────────────────────────────────────────────────────────────┤
│ 744:00:00                                                        │
└──────────────────────────────────────────────────────────────────┘
```
