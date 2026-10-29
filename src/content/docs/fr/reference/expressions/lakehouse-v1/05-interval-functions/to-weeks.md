---
title: TO_WEEKS (Lakehouse v1)
description: TO_WEEKS convertit un nombre donné de semaines en type Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-weeks.md
---

Convertit un nombre donné de semaines en type Interval.

- Accepte en entrée des entiers positifs, zéro et des entiers négatifs.

## Syntaxe Analyze

```python
func.to_weeks(<weeks>)
```

## Exemples Analyze

```python
func.to_weeks(2)
┌──────────────────────────────────────────────────────┐
│ func.to_weeks(2)                                     │
├──────────────────────────────────────────────────────┤
│ 14 days                                              │
└──────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_WEEKS(<weeks>)
```

## Type de retour

Interval (exprimé en jours).

## Exemples SQL

```sql
SELECT TO_WEEKS(2), TO_WEEKS(0), TO_WEEKS((- 2));

┌───────────────────────────────────────────┐
│ to_weeks(2) │ to_weeks(0) │ to_weeks(- 2) │
├─────────────┼─────────────┼───────────────┤
│ 14 days     │ 00:00:00    │ -14 days      │
└───────────────────────────────────────────┘
```
