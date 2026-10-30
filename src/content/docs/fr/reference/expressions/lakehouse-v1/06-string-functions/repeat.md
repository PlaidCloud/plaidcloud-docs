---
title: REPEAT (Lakehouse v1)
description: REPEAT renvoie une chaîne composée de la chaîne str répétée count fois.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/repeat.md
---

Renvoie une chaîne composée de la chaîne str répétée count fois. Si count est inférieur à 1, renvoie une chaîne vide. Renvoie NULL si str ou count est NULL.

## Syntaxe Analyze

```python
func.repeat(<str>, <count>)
```

## Exemples Analyze

```python
func.repeat(<str>, <count>)
┌─────────────────────────┐
│ func.repeat('plaid', 3) │
├─────────────────────────┤
│ plaidplaidplaid         │
└─────────────────────────┘
```

## Syntaxe SQL

```sql
REPEAT(<str>, <count>)
```

## Arguments

| Arguments | Description |
|-----------|-------------|
| `<str>`   | La chaîne.  |
| `<count>` | Le nombre.  |

## Exemples SQL

```sql
SELECT REPEAT('databend', 3);
┌──────────────────────────┐
│ REPEAT('databend', 3)    │
├──────────────────────────┤
│ databenddatabenddatabend │
└──────────────────────────┘

SELECT REPEAT('databend', 0);
┌───────────────────────┐
│ REPEAT('databend', 0) │
├───────────────────────┤
│                       │
└───────────────────────┘

SELECT REPEAT('databend', NULL);
┌──────────────────────────┐
│ REPEAT('databend', NULL) │
├──────────────────────────┤
│                     NULL │
└──────────────────────────┘
```
