---
title: ASCII (Lakehouse v1)
description: ASCII renvoie la valeur numérique du caractère le plus à gauche de la chaîne str.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/ascii.md
---

Renvoie la valeur numérique du caractère le plus à gauche de la chaîne str.

## Syntaxe Analyze

```python
func.ascii(<expr>)
```

## Exemples Analyze

```python
func.ascii('2')
┌─────────────────┐
│ func.ascii('2') │
├─────────────────┤
│              50 │
└─────────────────┘
```

## Syntaxe SQL

```sql
ASCII(<expr>)
```

## Arguments

| Arguments | Description |
|-----------|-------------|
| `<expr>`  | La chaîne.  |

## Type de retour

`TINYINT`

## Exemples SQL

```sql
SELECT ASCII('2');
┌────────────┐
│ ASCII('2') │
├────────────┤
│         50 │
└────────────┘
```
