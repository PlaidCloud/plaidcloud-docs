---
title: TO_WEEK_OF_YEAR (Lakehouse v1)
description: TO_WEEK_OF_YEAR calcule le numéro de semaine dans l'année pour une date donnée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-week-of-year.md
---

Calcule le numéro de semaine dans l'année pour une date donnée.

La numérotation ISO des semaines fonctionne ainsi : le 4 janvier appartient toujours à la première semaine. Si le 1er janvier tombe un jeudi, la semaine qui s'étend du lundi 29 décembre au dimanche 4 janvier est la semaine ISO 1. Si le 1er janvier tombe un vendredi, la semaine qui va du lundi 4 janvier au dimanche 10 janvier est la semaine ISO 1.

## Syntaxe Analyze

```python
func.to_week_of_year(<expr>)
```

## Exemples Analyze

```python
func.now(), func.to_week_of_year(func.now()), func.week(func.now()), func.weekofyear(func.now())

┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_week_of_year(func.now()) │ func.week(func.now()) │ func.weekofyear(func.now()) │
├────────────────────────────┼──────────────────────────────────┼───────────────────────┼─────────────────────────────┤
│ 2024-03-14 23:30:04.011624 │                               11 │                    11 │                          11 │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_WEEK_OF_YEAR(<expr>)
```

## Arguments

| Arguments | Description    |
|-----------|----------------|
| `<expr>`  | date/timestamp |

## Alias

- [WEEK](../week)
- [WEEKOFYEAR](../weekofyear)

## Type de retour

Renvoie un entier qui représente le numéro de semaine dans l'année, compris entre 1 et 53.

## Exemples SQL

```sql
SELECT NOW(), TO_WEEK_OF_YEAR(NOW()), WEEK(NOW()), WEEKOFYEAR(NOW());

┌───────────────────────────────────────────────────────────────────────────────────────┐
│            now()           │ to_week_of_year(now()) │ week(now()) │ weekofyear(now()) │
├────────────────────────────┼────────────────────────┼─────────────┼───────────────────┤
│ 2024-03-14 23:30:04.011624 │                     11 │          11 │                11 │
└───────────────────────────────────────────────────────────────────────────────────────┘
```
