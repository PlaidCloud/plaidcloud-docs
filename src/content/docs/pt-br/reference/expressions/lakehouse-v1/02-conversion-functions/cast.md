---
title: "CAST, :: (Lakehouse v1)"
description: "CAST, :: converte um valor de um tipo de dados para outro."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/cast.md
---

Converte um valor de um tipo de dados para outro. `::` é um alias de CAST.

Veja também: [TRY_CAST](../try-cast)

## Sintaxe do Analyze

```python
func.cast( <expr>, <data_type> )
```

## Exemplos do Analyze

```python
func.cast(1, string), func.to_string(1)

┌───────────────────────────────────────────┐
│ func.cast(1, string) │ func.to_string(1)  │
├──────────────────────┼────────────────────┤
│ 1                    │ 1                  │
└───────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
CAST( <expr> AS <data_type> )

<expr>::<data_type>
```

## Exemplos de SQL

```sql
SELECT CAST(1 AS VARCHAR), 1::VARCHAR;

┌───────────────────────────────┐
│ cast(1 as string) │ 1::string │
├───────────────────┼───────────┤
│ 1                 │ 1         │
└───────────────────────────────┘
```
