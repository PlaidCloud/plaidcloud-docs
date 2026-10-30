---
title: BIT_SHIFT_LEFT (Lakehouse v2)
description: BIT_SHIFT_LEFT — décale vers la gauche les bits d'une valeur numérique d'un nombre de positions donné.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bit-shift-left.md
---

Décale vers la gauche les bits d'une valeur numérique d'un nombre de positions donné.

## Syntaxe Analyze

```python
func.bit_shift_left(<value>, <shift>)
```

## Exemples Analyze

```python
func.bit_shift_left(1, 4)

┌────┐
│ 16  │
└────┘
```

## Syntaxe SQL

```sql
BIT_SHIFT_LEFT(<value>, <shift>)
```

## Exemples SQL

```sql
SELECT BIT_SHIFT_LEFT(1, 4);

┌────┐
│ 16  │
└────┘
```
