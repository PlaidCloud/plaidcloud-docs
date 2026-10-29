---
title: LOWER (Lakehouse v1)
description: LOWER renvoie une chaîne dont tous les caractères sont convertis en minuscules.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/lower.md
---

Renvoie une chaîne dont tous les caractères sont convertis en minuscules.

## Syntaxe Analyze

```python
func.lower(<str>)
```

## Exemples Analyze

```python
func.lower('Hello, PlaidCloud!')
┌──────────────────────────────────┐
│ func.lower('Hello, PlaidCloud!') │
├──────────────────────────────────┤
│ hello, plaidcloud!               │
└──────────────────────────────────┘
```

## Syntaxe SQL

```sql
LOWER(<str>)
```

## Alias

- [LCASE](../lcase)

## Type de retour

VARCHAR

## Exemples SQL

```sql
SELECT LOWER('Hello, Databend!'), LCASE('Hello, Databend!');

┌───────────────────────────────────────────────────────┐
│ lower('hello, databend!') │ lcase('hello, databend!') │
├───────────────────────────┼───────────────────────────┤
│ hello, databend!          │ hello, databend!          │
└───────────────────────────────────────────────────────┘
```
