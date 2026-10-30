---
title: TO_QUARTER (Lakehouse v1)
description: TO_QUARTER — obtém o trimestre (1, 2, 3 ou 4) de uma data ou carimbo de data/hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-quarter.md
---

Obtém o trimestre (1, 2, 3 ou 4) de uma data ou carimbo de data/hora.

## Sintaxe do Analyze

```python
func.to_quarter(<expr>)
```

## Exemplos do Analyze

```python
func.now(), func.to_quarter(func.now()), func.quarter(func.now())

┌─────────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_quarter(func.now()) │ func.quarter(func.now()) │
├────────────────────────────┼─────────────────────────────┼──────────────────────────┤
│ 2024-03-14 23:32:52.743133 │                           3 │                        3 │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_QUARTER( <date_or_time_expr> )
```

## Aliases

- [QUARTER](../quarter)

## Tipo de retorno

Número inteiro.

## Exemplos SQL

```sql
SELECT NOW(), TO_QUARTER(NOW()), QUARTER(NOW());

┌─────────────────────────────────────────────────────────────────┐
│            now()           │ to_quarter(now()) │ quarter(now()) │
├────────────────────────────┼───────────────────┼────────────────┤
│ 2024-03-14 23:32:52.743133 │                 1 │              1 │
└─────────────────────────────────────────────────────────────────┘
```
