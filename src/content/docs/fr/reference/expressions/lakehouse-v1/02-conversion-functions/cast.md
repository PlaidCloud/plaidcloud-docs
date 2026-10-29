---
title: "CAST, :: (Lakehouse v1)"
description: "CAST, :: : convertit une valeur d'un type de données à un autre."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/cast.md
---

Convertit une valeur d'un type de données à un autre. `::` est un alias de CAST.

Voir aussi : [TRY_CAST](../try-cast)

## Syntaxe Analyze

```python
func.cast( <expr>, <data_type> )
```

## Exemples Analyze

```python
func.cast(1, string), func.to_string(1)

┌───────────────────────────────────────────┐
│ func.cast(1, string) │ func.to_string(1)  │
├──────────────────────┼────────────────────┤
│ 1                    │ 1                  │
└───────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
CAST( <expr> AS <data_type> )

<expr>::<data_type>
```

## Exemples SQL

```sql
SELECT CAST(1 AS VARCHAR), 1::VARCHAR;

┌───────────────────────────────┐
│ cast(1 as string) │ 1::string │
├───────────────────┼───────────┤
│ 1                 │ 1         │
└───────────────────────────────┘
```
