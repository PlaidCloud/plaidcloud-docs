---
title: TO_HOUR (Lakehouse v1)
description: TO_HOUR — convertit une date avec heure (horodatage/datetime) en nombre UInt8 contenant l'heure au format 24 heures (0-23).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-hour.md
---

Convertit une date avec heure (horodatage/datetime) en nombre UInt8 contenant l'heure au format 24 heures (0-23).
Cette fonction suppose que, lorsque les horloges avancent, c'est d'une heure à 2 h du matin, et que, lorsqu'elles reculent, c'est d'une heure à 3 h du matin (ce qui n'est pas toujours vrai : à Moscou, par exemple, les horloges ont été changées deux fois à des moments différents).


## Syntaxe Analyze

```python
func.to_hour(<expr>)
```

## Exemples Analyze

```python
func.to_hour('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_hour('2023-11-12 09:38:18.165575')         │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                  9 │
└────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_HOUR(<expr>)
```

## Arguments

| Arguments | Description |
|-----------|-------------|
| `<expr>`  | horodatage  |

## Type de retour

`TINYINT`

## Exemples SQL

```sql
SELECT
    to_hour('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────┐
│ to_hour('2023-11-12 09:38:18.165575') │
│                 UInt8                 │
├───────────────────────────────────────┤
│                                     9 │
└───────────────────────────────────────┘
```
