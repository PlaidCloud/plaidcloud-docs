---
title: FMOD (Lakehouse v2)
description: FMOD — zwraca resztę zmiennoprzecinkową z dzielenia dwóch liczb.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/fmod.md
---

Zwraca resztę zmiennoprzecinkową z dzielenia dwóch liczb.

## Składnia Analyze

```python
func.fmod(<x>, <y>)
```

## Przykłady Analyze

```python
func.fmod(10.5, 3.0)

┌─────┐
│ 1.5  │
└─────┘
```

## Składnia SQL

```sql
FMOD(<x>, <y>)
```

## Przykłady SQL

```sql
SELECT FMOD(10.5, 3.0);

┌─────┐
│ 1.5  │
└─────┘
```
