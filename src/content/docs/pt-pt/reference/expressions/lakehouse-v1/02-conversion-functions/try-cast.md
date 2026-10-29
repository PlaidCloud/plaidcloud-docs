---
title: TRY_CAST (Lakehouse v1)
description: TRY_CAST — converte um valor de um tipo de dados para outro.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/try-cast.md
---

Converte um valor de um tipo de dados para outro. Devolve NULL em caso de erro.

Ver também: [CAST](../cast)

## Sintaxe do Analyze

```python
func.try_cast( <expr>, <data_type> )
```

## Exemplos do Analyze

```python
func.try_cast(1, string)

┌──────────────────────────┐
│ func.try_cast(1, string) │
├──────────────────────────┤
│ 1                        │
└──────────────────────────┘
```

## Sintaxe SQL

```sql
TRY_CAST( <expr> AS <data_type> )
```

## Exemplos SQL

```sql
SELECT TRY_CAST(1 AS VARCHAR);

┌───────────────────────┐
│ try_cast(1 as string) │
├───────────────────────┤
│ 1                     │
└───────────────────────┘
```
