---
title: LEAST (Lakehouse v1)
description: LEAST — renvoie la valeur minimale d'un ensemble de valeurs.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/least.md
---

Renvoie la valeur minimale d'un ensemble de valeurs.

## Syntaxe Analyze

```python
func.least((<value1>, <value2> ...))
```

## Exemples Analyze

```python
func.least((5, 9, 4))

┌───────────────────────┐
│ func.least((5, 9, 4)) │
├───────────────────────┤
│                     4 │
└───────────────────────┘
```

## Syntaxe SQL

```sql
LEAST(<value1>, <value2> ...)
```

## Exemples SQL

```sql
SELECT LEAST(5, 9, 4);

┌────────────────┐
│ least(5, 9, 4) │
├────────────────┤
│              4 │
└────────────────┘
```
