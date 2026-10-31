---
title: RPAD (Lakehouse v2)
description: RPAD — complète une chaîne à droite jusqu'à une longueur donnée avec une chaîne de remplissage.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/rpad.md
---

Complète une chaîne à droite jusqu'à une longueur donnée avec une chaîne de remplissage.

## Syntaxe Analyze

```python
func.rpad(<str>, <len>, <pad>)
```

## Exemples Analyze

```python
func.rpad('hello', 10, '.')

┌──────────────┐
│ 'hello.....'  │
└──────────────┘
```

## Syntaxe SQL

```sql
RPAD(<str>, <len>, <pad>)
```

## Exemples SQL

```sql
SELECT RPAD('hello', 10, '.');

┌────────────┐
│ hello.....  │
└────────────┘
```
