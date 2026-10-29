---
title: LPAD (Lakehouse v2)
description: LPAD — complète une chaîne à gauche jusqu'à une longueur donnée avec une chaîne de remplissage.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/lpad.md
---

Complète une chaîne à gauche jusqu'à une longueur donnée avec une chaîne de remplissage.

## Syntaxe Analyze

```python
func.lpad(<str>, <len>, <pad>)
```

## Exemples Analyze

```python
func.lpad('42', 5, '0')

┌─────────┐
│ '00042'  │
└─────────┘
```

## Syntaxe SQL

```sql
LPAD(<str>, <len>, <pad>)
```

## Exemples SQL

```sql
SELECT LPAD('42', 5, '0');

┌───────┐
│ 00042  │
└───────┘
```
