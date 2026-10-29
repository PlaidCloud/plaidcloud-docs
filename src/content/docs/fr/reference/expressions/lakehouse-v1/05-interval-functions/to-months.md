---
title: TO_MONTHS (Lakehouse v1)
description: TO_MONTHS convertit un nombre donné de mois en type Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-months.md
---

Convertit un nombre donné de mois en type Interval.

- Accepte en entrée des entiers positifs, zéro et des entiers négatifs.

## Syntaxe Analyze

```python
func.to_months(<months>)
```

## Exemples Analyze

```python
func.to_months(2)
┌──────────────────────────────────────────────────────┐
│ func.to_months(2)                                    │
├──────────────────────────────────────────────────────┤
│ 2 months                                             │
└──────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_MONTHS(<months>)
```

## Type de retour

Interval (exprimé en mois).

## Exemples SQL

```sql
SELECT TO_MONTHS(2), TO_MONTHS(0), TO_MONTHS((- 2));

┌──────────────────────────────────────────────┐
│ to_months(2) │ to_months(0) │ to_months(- 2) │
├──────────────┼──────────────┼────────────────┤
│ 2 months     │ 00:00:00     │ -2 months      │
└──────────────────────────────────────────────┘
```
