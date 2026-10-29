---
title: TO_DECADES (Lakehouse v1)
description: TO_DECADES convertit un nombre donné de décennies en type Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-decades.md
---

Convertit un nombre donné de décennies en type Interval.

- Accepte en entrée des entiers positifs, zéro et des entiers négatifs.

## Syntaxe Analyze

```python
func.to_decades(<decades>)
```

## Exemples Analyze

```python
func.to_decades(2)
┌──────────────────────────────────────────────────────┐
│ func.to_decades(2)                                   │
├──────────────────────────────────────────────────────┤
│ 20 years                                             │
└──────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_DECADES(<decades>)
```

## Type de retour

Interval (exprimé en années).

## Exemples SQL

```sql
SELECT TO_DECADES(2), TO_DECADES(0), TO_DECADES((- 2));

┌─────────────────────────────────────────────────┐
│ to_decades(2) │ to_decades(0) │ to_decades(- 2) │
├───────────────┼───────────────┼─────────────────┤
│ 20 years      │ 00:00:00      │ -20 years       │
└─────────────────────────────────────────────────┘
```
