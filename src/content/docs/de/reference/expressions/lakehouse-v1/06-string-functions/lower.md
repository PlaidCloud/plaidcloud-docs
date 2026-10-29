---
title: LOWER (Lakehouse v1)
description: LOWER – gibt eine Zeichenfolge zurück, in der alle Zeichen in Kleinbuchstaben umgewandelt wurden.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/lower.md
---

Gibt eine Zeichenfolge zurück, in der alle Zeichen in Kleinbuchstaben umgewandelt wurden.

## Analyze-Syntax

```python
func.lower(<str>)
```

## Analyze-Beispiele

```python
func.lower('Hello, PlaidCloud!')
┌──────────────────────────────────┐
│ func.lower('Hello, PlaidCloud!') │
├──────────────────────────────────┤
│ hello, plaidcloud!               │
└──────────────────────────────────┘
```

## SQL-Syntax

```sql
LOWER(<str>)
```

## Aliase

- [LCASE](../lcase)

## Rückgabetyp

VARCHAR

## SQL-Beispiele

```sql
SELECT LOWER('Hello, Databend!'), LCASE('Hello, Databend!');

┌───────────────────────────────────────────────────────┐
│ lower('hello, databend!') │ lcase('hello, databend!') │
├───────────────────────────┼───────────────────────────┤
│ hello, databend!          │ hello, databend!          │
└───────────────────────────────────────────────────────┘
```
