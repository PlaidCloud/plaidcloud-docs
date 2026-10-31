---
title: BIT_LENGTH (Lakehouse v1)
description: BIT_LENGTH renvoie la longueur d'une chaîne en bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/bit-length.md
---

Renvoie la longueur d'une chaîne en bits.

## Syntaxe Analyze

```python
func.bit_length(<expr>)
```

## Exemples Analyze

```python
func.bit_length('Word')
┌─────────────────────────┐
│ func.bit_length('Word') │
├─────────────────────────┤
│                      32 │
└─────────────────────────┘
```

## Syntaxe SQL

```sql
BIT_LENGTH(<expr>)
```

## Arguments

| Arguments | Description |
|-----------| ----------- |
| `<expr>`  | La chaîne.  |

## Type de retour

`BIGINT`

## Exemples SQL

```sql
SELECT BIT_LENGTH('Word');
┌────────────────────────────┐
│ SELECT BIT_LENGTH('Word'); │
├────────────────────────────┤
│ 32                         │
└────────────────────────────┘
```
