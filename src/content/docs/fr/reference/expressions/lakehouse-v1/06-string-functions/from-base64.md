---
title: FROM_BASE64 (Lakehouse v1)
description: FROM_BASE64 prend une chaîne encodée selon les règles base64 et renvoie le résultat décodé sous forme binaire.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/from-base64.md
---

Prend une chaîne encodée selon les règles base64 et renvoie le résultat décodé sous forme binaire.
Le résultat est NULL si l'argument est NULL ou n'est pas une chaîne base64 valide.

## Syntaxe Analyze

```python
func.from_base64(<expr>)
```

## Exemples Analyze

```python
func.from_base64('YWJj')
┌──────────────────────────┐
│ func.from_base64('YWJj') │
├──────────────────────────┤
│ abc                      │
└──────────────────────────┘
```

## Syntaxe SQL

```sql
FROM_BASE64(<expr>)
```

## Arguments

| Arguments | Description           |
|-----------|-----------------------|
| `<expr>`  | La valeur de chaîne.  |

## Type de retour

`BINARY`

## Exemples SQL

```sql
SELECT TO_BASE64('abc'), FROM_BASE64(TO_BASE64('abc')) as b, b::String;
┌───────────────────────────────────────┐
│ to_base64('abc') │    b   │ b::string │
│      String      │ Binary │   String  │
├──────────────────┼────────┼───────────┤
│ YWJj             │ 616263 │ abc       │
└───────────────────────────────────────┘
```
