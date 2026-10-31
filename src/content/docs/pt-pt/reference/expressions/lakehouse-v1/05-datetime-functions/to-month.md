---
title: TO_MONTH (Lakehouse v1)
description: TO_MONTH — converte uma data ou data com hora (timestamp/datetime) num número UInt8 que contém o mês.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-month.md
---

Converte uma data ou data com hora (timestamp/datetime) num número UInt8 que contém o número do mês (1-12).

## Sintaxe do Analyze

```python
func.to_month(<expr>)
```

## Exemplos do Analyze

```python
func.now(), func.to_month(func.now()), func.month(func.now())

┌─────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_month(func.now()) │ func.month(func.now()) │
├────────────────────────────┼───────────────────────────┼────────────────────────┤
│ 2024-03-14 23:34:02.161291 │                         3 │                      3 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_MONTH(<expr>)
```

## Argumentos

| Argumentos | Descrição            |
|-----------|----------------------|
| `<expr>`  | data/carimbo de data/hora |

## Aliases

- [MONTH](../month)

## Tipo de retorno

 `TINYINT`

## Exemplos SQL

```sql
SELECT NOW(), TO_MONTH(NOW()), MONTH(NOW());

┌─────────────────────────────────────────────────────────────┐
│            now()           │ to_month(now()) │ month(now()) │
├────────────────────────────┼─────────────────┼──────────────┤
│ 2024-03-14 23:34:02.161291 │               3 │            3 │
└─────────────────────────────────────────────────────────────┘
```
