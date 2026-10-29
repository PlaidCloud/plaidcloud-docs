---
title: TO_HOURS (Lakehouse v1)
description: TO_HOURS convertit un nombre donné d'heures en type Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-hours.md
---

Convertit un nombre donné d'heures en type Interval.

- Accepte en entrée des entiers positifs, zéro et des entiers négatifs.

## Syntaxe Analyze

```python
func.to_hours(<hours>)
```

## Exemples Analyze

```python
func.to_hours(2)
┌──────────────────────────────────────────────────────┐
│ func.to_hours(2)                                     │
├──────────────────────────────────────────────────────┤
│ 2:00:00                                              │
└──────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_HOURS(<hours>)
```

## Type de retour

Interval (au format `hh:mm:ss`).

## Exemples SQL

```sql
SELECT TO_HOURS(2), TO_HOURS(0), TO_HOURS((- 2));

┌───────────────────────────────────────────┐
│ to_hours(2) │ to_hours(0) │ to_hours(- 2) │
├─────────────┼─────────────┼───────────────┤
│ 2:00:00     │ 00:00:00    │ -2:00:00      │
└───────────────────────────────────────────┘
```
