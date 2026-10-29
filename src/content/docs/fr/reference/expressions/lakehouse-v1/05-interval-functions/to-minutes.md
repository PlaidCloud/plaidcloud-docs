---
title: TO_MINUTES (Lakehouse v1)
description: TO_MINUTES convertit un nombre donné de minutes en type Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-minutes.md
---

Convertit un nombre donné de minutes en type Interval.

- Accepte en entrée des entiers positifs, zéro et des entiers négatifs.

## Syntaxe Analyze

```python
func.to_minutes(<minutes>)
```

## Exemples Analyze

```python
func.to_minutes(2)
┌──────────────────────────────────────────────────────┐
│ func.to_minutes(2)                                   │
├──────────────────────────────────────────────────────┤
│ 0:02:00                                              │
└──────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_MINUTES(<minutes>)
```

## Type de retour

Interval (au format `hh:mm:ss`).

## Exemples SQL

```sql
SELECT TO_MINUTES(2), TO_MINUTES(0), TO_MINUTES((- 2));

┌─────────────────────────────────────────────────┐
│ to_minutes(2) │ to_minutes(0) │ to_minutes(- 2) │
├───────────────┼───────────────┼─────────────────┤
│ 0:02:00       │ 00:00:00      │ -0:02:00        │
└─────────────────────────────────────────────────┘
```
