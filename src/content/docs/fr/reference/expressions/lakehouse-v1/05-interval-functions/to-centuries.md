---
title: TO_CENTURIES (Lakehouse v1)
description: TO_CENTURIES convertit un nombre donné de siècles en type Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-centuries.md
---

Convertit un nombre donné de siècles en type Interval.

- Accepte en entrée des entiers positifs, zéro et des entiers négatifs.

## Syntaxe Analyze

```python
func.to_centuries(<centuries>)
```

## Exemples Analyze

```python
func.to_centuries(2)
┌──────────────────────────────────────────────────────┐
│ func.to_centuries(2)                                 │
├──────────────────────────────────────────────────────┤
│ 200 years                                            │
└──────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_CENTURIES(<centuries>)
```

## Type de retour

Interval (exprimé en années).

## Exemples SQL

```sql
SELECT TO_CENTURIES(2), TO_CENTURIES(0), TO_CENTURIES(-2);

┌───────────────────────────────────────────────────────┐
│ to_centuries(2) │ to_centuries(0) │ to_centuries(- 2) │
├─────────────────┼─────────────────┼───────────────────┤
│ 200 years       │ 00:00:00        │ -200 years        │
└───────────────────────────────────────────────────────┘
```
