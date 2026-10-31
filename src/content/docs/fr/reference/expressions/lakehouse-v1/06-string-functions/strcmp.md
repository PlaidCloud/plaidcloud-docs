---
title: STRCMP (Lakehouse v1)
description: STRCMP renvoie 0 si les chaînes sont identiques, -1 si le premier argument est inférieur au second, et 1 sinon.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/strcmp.md
---

Renvoie 0 si les chaînes sont identiques, -1 si le premier argument est inférieur au second, et 1 sinon.

## Syntaxe Analyze

```python
func.strcmp(<expr1> ,<expr2>)
```

## Exemples Analyze

```python
func.strcmp('text', 'text2')
┌──────────────────────────────┐
│ func.strcmp('text', 'text2') │
├──────────────────────────────┤
│                           -1 │
└──────────────────────────────┘

func.strcmp('text2', 'text')
┌──────────────────────────────┐
│ func.strcmp('text2', 'text') │
├──────────────────────────────┤
│                            1 │
└──────────────────────────────┘

func.strcmp('text', 'text')
┌──────────────────────────────┐
│ func.strcmp('text', 'text')  │
├──────────────────────────────┤
│                            0 │
└──────────────────────────────┘
```

## Syntaxe SQL

```sql
STRCMP(<expr1> ,<expr2>)
```

## Arguments

| Arguments | Description |
|-----------|-------------|
| `<expr1>` | La chaîne.  |
| `<expr2>` | La chaîne.  |

## Type de retour

`BIGINT`

## Exemples SQL

```sql
SELECT STRCMP('text', 'text2');
┌─────────────────────────┐
│ STRCMP('text', 'text2') │
├─────────────────────────┤
│                      -1 │
└─────────────────────────┘

SELECT STRCMP('text2', 'text');
┌─────────────────────────┐
│ STRCMP('text2', 'text') │
├─────────────────────────┤
│                       1 │
└─────────────────────────┘

SELECT STRCMP('text', 'text');
┌────────────────────────┐
│ STRCMP('text', 'text') │
├────────────────────────┤
│                      0 │
└────────────────────────┘
```
