---
title: TO_SECONDS (Lakehouse v1)
description: TO_SECONDS convertit un nombre donné de secondes en type Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-seconds.md
---

Convertit un nombre donné de secondes en type Interval.

- Accepte en entrée des entiers positifs, zéro et des entiers négatifs.

## Syntaxe Analyze

```python
func.to_seconds(<seconds>)
```

## Exemples Analyze

```python
func.to_seconds(2)
┌──────────────────────────────────────────────────────┐
│ func.to_seconds(2)                                   │
├──────────────────────────────────────────────────────┤
│ 0:00:02                                              │
└──────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_SECONDS(<seconds>)
```

## Alias

- [EPOCH](../epoch)

## Type de retour

Interval (au format `hh:mm:ss`).

## Exemples SQL

```sql
SELECT TO_SECONDS(2), TO_SECONDS(0), TO_SECONDS((- 2));

┌─────────────────────────────────────────────────┐
│ to_seconds(2) │ to_seconds(0) │ to_seconds(- 2) │
├───────────────┼───────────────┼─────────────────┤
│ 0:00:02       │ 00:00:00      │ -0:00:02        │
└─────────────────────────────────────────────────┘
```
