---
title: TO_MILLENNIA (Lakehouse v1)
description: TO_MILLENNIA convertit un nombre donné de millénaires en type Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-millennia.md
---

Convertit un nombre donné de millénaires en type Interval.

- Accepte en entrée des entiers positifs, zéro et des entiers négatifs.

## Syntaxe Analyze

```python
func.to_millennia(<millennia>)
```

## Exemples Analyze

```python
func.to_millennia(2)
┌──────────────────────────────────────────────────────┐
│ func.to_millennia(2)                                 │
├──────────────────────────────────────────────────────┤
│ 2000 years                                            │
└──────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_MILLENNIA(<millennia>)
```

## Type de retour

Interval (exprimé en années).

## Exemples SQL

```sql
SELECT TO_MILLENNIA(2), TO_MILLENNIA(0), TO_MILLENNIA((- 2));

┌───────────────────────────────────────────────────────┐
│ to_millennia(2) │ to_millennia(0) │ to_millennia(- 2) │
├─────────────────┼─────────────────┼───────────────────┤
│ 2000 years      │ 00:00:00        │ -2000 years       │
└───────────────────────────────────────────────────────┘
```
