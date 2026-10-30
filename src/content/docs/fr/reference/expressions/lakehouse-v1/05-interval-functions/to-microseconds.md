---
title: TO_MICROSECONDS (Lakehouse v1)
description: TO_MICROSECONDS convertit un nombre donné de microsecondes en type Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-microseconds.md
---

Convertit un nombre donné de microsecondes en type Interval.

- Accepte en entrée des entiers positifs, zéro et des entiers négatifs.

## Syntaxe Analyze

```python
func.to_microseconds(<microseconds>)
```

## Exemples Analyze

```python
func.to_microseconds(2)
┌──────────────────────────────────────────────────────┐
│ func.to_microseconds(2)                              │
├──────────────────────────────────────────────────────┤
│ 0:00:00.000002                                       │
└──────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_MICROSECONDS(<microseconds>)
```

## Type de retour

Interval (au format `hh:mm:ss.sssssss`).

## Exemples SQL

```sql
SELECT TO_MICROSECONDS(2), TO_MICROSECONDS(0), TO_MICROSECONDS((- 2));

┌────────────────────────────────────────────────────────────────┐
│ to_microseconds(2) │ to_microseconds(0) │ to_microseconds(- 2) │
├────────────────────┼────────────────────┼──────────────────────┤
│ 0:00:00.000002     │ 00:00:00           │ -0:00:00.000002      │
└────────────────────────────────────────────────────────────────┘
```
