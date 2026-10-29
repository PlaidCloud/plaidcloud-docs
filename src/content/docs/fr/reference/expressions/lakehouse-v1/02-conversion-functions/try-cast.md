---
title: TRY_CAST (Lakehouse v1)
description: "TRY_CAST : convertit une valeur d'un type de données à un autre."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/try-cast.md
---

Convertit une valeur d'un type de données à un autre. Renvoie NULL en cas d'erreur.

Voir aussi : [CAST](../cast)

## Syntaxe Analyze

```python
func.try_cast( <expr>, <data_type> )
```

## Exemples Analyze

```python
func.try_cast(1, string)

┌──────────────────────────┐
│ func.try_cast(1, string) │
├──────────────────────────┤
│ 1                        │
└──────────────────────────┘
```

## Syntaxe SQL

```sql
TRY_CAST( <expr> AS <data_type> )
```

## Exemples SQL

```sql
SELECT TRY_CAST(1 AS VARCHAR);

┌───────────────────────┐
│ try_cast(1 as string) │
├───────────────────────┤
│ 1                     │
└───────────────────────┘
```
