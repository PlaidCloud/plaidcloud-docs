---
title: TRUNCATE (Lakehouse v1)
description: TRUNCATE — renvoie le nombre x tronqué à d décimales.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/truncate.md
---

Renvoie le nombre `x` tronqué à `d` décimales. Si `d` vaut 0, le résultat n'a ni virgule ni partie fractionnaire. `d` peut être négatif pour mettre à zéro `d` chiffres à gauche de la virgule de la valeur `x`. La valeur absolue maximale de `d` est 30 ; tout chiffre au-delà de 30 (ou -30) est tronqué.

## Syntaxe Analyze

```python
func.truncate( <x, d> )
```

## Exemples Analyze

```python
func.truncate(1.223, 1)

┌─────────────────────────┐
│ func.truncate(1.223, 1) │
├─────────────────────────┤
│                     1.2 │
└─────────────────────────┘
```

## Syntaxe SQL

```sql
TRUNCATE( <x, d> )
```

## Exemples SQL

```sql
SELECT TRUNCATE(1.223, 1);

┌────────────────────┐
│ truncate(1.223, 1) │
├────────────────────┤
│ 1.2                │
└────────────────────┘
```
