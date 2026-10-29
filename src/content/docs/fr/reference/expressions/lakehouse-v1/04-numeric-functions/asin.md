---
title: ASIN (Lakehouse v1)
description: ASIN — renvoie l'arc sinus de x, c'est-à-dire la valeur dont le sinus est x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/asin.md
---

Renvoie l'arc sinus de `x`, c'est-à-dire la valeur dont le sinus est `x`. Renvoie NULL si `x` n'est pas compris entre -1 et 1.

## Syntaxe Analyze

```python
func.asin( <x> )
```

## Exemples Analyze

```python
func.asin(0.2)

┌────────────────────┐
│   func.asin(0.2)   │
├────────────────────┤
│ 0.2013579207903308 │
└────────────────────┘
```

## Syntaxe SQL

```sql
ASIN( <x> )
```

## Exemples SQL

```sql
SELECT ASIN(0.2);

┌────────────────────┐
│      asin(0.2)     │
├────────────────────┤
│ 0.2013579207903308 │
└────────────────────┘
```
