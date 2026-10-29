---
title: BIT_SHIFT_RIGHT (Lakehouse v2)
description: "Utilisez la fonction binaire BIT_SHIFT_RIGHT dans PlaidCloud Lakehouse. Décale vers la droite les bits d'une valeur numérique d'un nombre de positions donné (décalage arithmétique)."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bit-shift-right.md
---

Décale vers la droite les bits d'une valeur numérique d'un nombre de positions donné (décalage arithmétique).

## Syntaxe Analyze

```python
func.bit_shift_right(<value>, <shift>)
```

## Exemples Analyze

```python
func.bit_shift_right(16, 2)

┌───┐
│ 4  │
└───┘
```

## Syntaxe SQL

```sql
BIT_SHIFT_RIGHT(<value>, <shift>)
```

## Exemples SQL

```sql
SELECT BIT_SHIFT_RIGHT(16, 2);

┌───┐
│ 4  │
└───┘
```
