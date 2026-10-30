---
title: BIN (Lakehouse v1)
description: BIN renvoie la représentation sous forme de chaîne de la valeur binaire de N.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/bin.md
---

Renvoie la représentation sous forme de chaîne de la valeur binaire de N.

## Syntaxe Analyze

```python
func.bin(<expr>)
```

## Exemples Analyze

```python
func.bin(12)
┌──────────────┐
│ func.bin(12) │
├──────────────┤
│ 1100         │
└──────────────┘
```

## Syntaxe SQL

```sql
BIN(<expr>)
```

## Arguments

| Arguments | Description |
|-----------|-------------|
| `<expr>`  | Le nombre.  |

## Type de retour

`VARCHAR`

## Exemples SQL

```sql
SELECT BIN(12);
┌─────────┐
│ BIN(12) │
├─────────┤
│ 1100    │
└─────────┘
```
