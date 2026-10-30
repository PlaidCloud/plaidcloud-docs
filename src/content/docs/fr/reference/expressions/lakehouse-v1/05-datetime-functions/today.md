---
title: TODAY (Lakehouse v1)
description: TODAY renvoie la date du jour.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/today.md
---

Renvoie la date du jour.

## Syntaxe Analyze

```python
func.today()
```

## Exemples Analyze

```python
func.today()
┌──────────────┐
│ func.today() │
├──────────────┤
│ 2021-09-03   │
└──────────────┘
```

## Syntaxe SQL

```sql
TODAY()
```

## Type de retour

`DATE`, renvoie la date au format « YYYY-MM-DD ».

## Exemples SQL

```sql
SELECT TODAY();
┌────────────┐
│ TODAY()    │
├────────────┤
│ 2021-09-03 │
└────────────┘
```
