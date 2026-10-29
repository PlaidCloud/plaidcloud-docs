---
title: UPPER (Lakehouse v1)
description: "UPPER : renvoie une chaîne dont tous les caractères sont convertis en majuscules."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/upper.md
---

Renvoie une chaîne dont tous les caractères sont convertis en majuscules.

## Syntaxe Analyze

```python
func.unhex(<expr>)
```

## Exemples Analyze

```python
func.upper('hello, plaidcloud lakehouse!')
┌────────────────────────────────────────────┐
│ func.upper('hello, plaidcloud lakehouse!') │
├────────────────────────────────────────────┤
│ 'HELLO, PLAIDCLOUD LAKEHOUSE!'             │
└────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
UPPER(<str>)
```

## Alias

- [UCASE](../ucase)

## Type de retour

VARCHAR

## Exemples SQL

```sql
SELECT UPPER('hello, databend!'), UCASE('hello, databend!');

┌───────────────────────────────────────────────────────┐
│ upper('hello, databend!') │ ucase('hello, databend!') │
├───────────────────────────┼───────────────────────────┤
│ HELLO, DATABEND!          │ HELLO, DATABEND!          │
└───────────────────────────────────────────────────────┘
```
