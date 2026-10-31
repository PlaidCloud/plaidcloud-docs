---
title: BIT_SHIFT_RIGHT_LOGICAL (Lakehouse v2)
description: "Utilisez la fonction binaire BIT_SHIFT_RIGHT_LOGICAL dans PlaidCloud Lakehouse. Décale vers la droite les bits d'une valeur numérique d'un nombre de positions donné."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bit-shift-right-logical.md
---

Décale vers la droite les bits d'une valeur numérique d'un nombre de positions donné (décalage logique).

## Syntaxe Analyze

```python
func.bit_shift_right_logical(<value>, <shift>)
```

## Exemples Analyze

```python
func.bit_shift_right_logical(16, 2)

┌───┐
│ 4  │
└───┘
```

## Syntaxe SQL

```sql
BIT_SHIFT_RIGHT_LOGICAL(<value>, <shift>)
```

## Exemples SQL

```sql
SELECT BIT_SHIFT_RIGHT_LOGICAL(16, 2);

┌───┐
│ 4  │
└───┘
```
