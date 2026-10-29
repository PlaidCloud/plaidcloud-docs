---
title: TO_YEAR (Lakehouse v1)
description: TO_YEAR — converte uma data ou data com hora (timestamp/datetime) num número UInt16 que contém o ano.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-year.md
---

Converte uma data ou data com hora (timestamp/datetime) num número UInt16 que contém o número do ano (d.C.).

## Sintaxe do Analyze

```python
func.to_year(<expr>)
```

## Exemplos do Analyze

```python
func.now(), func.to_year(func.now()), func.year(func.now())

┌───────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_year(func.now()) │ func.year(func.now()) │
├────────────────────────────┼──────────────────────────┼───────────────────────┤
│ 2024-03-14 23:37:03.895166 │                     2024 │                  2024 │
└───────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_YEAR(<expr>)
```

## Argumentos

| Argumentos | Descrição      |
|-----------|----------------|
| `<expr>`  | data/timestamp |

## Aliases

- [YEAR](../year)

## Tipo de Retorno

 `SMALLINT`

## Exemplos SQL

```sql
SELECT NOW(), TO_YEAR(NOW()), YEAR(NOW());

┌───────────────────────────────────────────────────────────┐
│            now()           │ to_year(now()) │ year(now()) │
├────────────────────────────┼────────────────┼─────────────┤
│ 2024-03-14 23:37:03.895166 │           2024 │        2024 │
└───────────────────────────────────────────────────────────┘
```
