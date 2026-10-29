---
title: TO_YYYYMM (Lakehouse v1)
description: TO_YYYYMM — converte uma data ou data com hora (timestamp/datetime) em um número UInt32.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymm.md
---

Converte uma data ou data com hora (timestamp/datetime) em um número UInt32 que contém o ano e o mês.

## Sintaxe do Analyze

```python
func.to_yyyymm(<expr>)
```

## Exemplos do Analyze

```python
func.to_yyyymm('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────┐
│ func.to_yyyymm('2023-11-12 09:38:18.165575') │
│                   UInt32                     │
├──────────────────────────────────────────────┤
│                                       202311 │
└──────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_YYYYMM(<expr>)
```

## Argumentos

| Argumentos | Descrição      |
|-----------|----------------|
| `<expr>`  | data/timestamp |

## Tipo de retorno

`INT`, retorna no formato `YYYYMM`.

## Exemplos de SQL

```sql
SELECT
  to_yyyymm('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ to_yyyymm('2023-11-12 09:38:18.165575') │
│                  UInt32                 │
├─────────────────────────────────────────┤
│                                  202311 │
└─────────────────────────────────────────┘
```
