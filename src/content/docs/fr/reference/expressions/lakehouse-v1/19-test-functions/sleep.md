---
title: SLEEP (Lakehouse v1)
description: SLEEP — marque une pause de seconds secondes sur chaque bloc de données.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/19-test-functions/sleep.md
---

Marque une pause de `seconds` secondes sur chaque bloc de données.

!!! warning 
    À utiliser uniquement pour des tests nécessitant une pause.


## Syntaxe SQL

```sql
SLEEP(seconds)
```

## Arguments

| Arguments   | Description |
| ----------- | ----------- |
| seconds  | Doit être une colonne constante de tout nombre entier ou décimal non négatif.｜

## Type de retour

UInt8

## Exemples SQL

```sql
SELECT sleep(2);
┌──────────┐
│ sleep(2) │
├──────────┤
│        0 │
└──────────┘
```
