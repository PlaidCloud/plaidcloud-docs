---
title: UPPER (Lakehouse v1)
description: UPPER – gibt eine Zeichenfolge zurück, in der alle Zeichen in Großbuchstaben umgewandelt wurden.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/upper.md
---

Gibt eine Zeichenfolge zurück, in der alle Zeichen in Großbuchstaben umgewandelt wurden.

## Analyze-Syntax

```python
func.unhex(<expr>)
```

## Analyze-Beispiele

```python
func.upper('hello, plaidcloud lakehouse!')
┌────────────────────────────────────────────┐
│ func.upper('hello, plaidcloud lakehouse!') │
├────────────────────────────────────────────┤
│ 'HELLO, PLAIDCLOUD LAKEHOUSE!'             │
└────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
UPPER(<str>)
```

## Aliasse

- [UCASE](../ucase)

## Rückgabetyp

VARCHAR

## SQL-Beispiele

```sql
SELECT UPPER('hello, databend!'), UCASE('hello, databend!');

┌───────────────────────────────────────────────────────┐
│ upper('hello, databend!') │ ucase('hello, databend!') │
├───────────────────────────┼───────────────────────────┤
│ HELLO, DATABEND!          │ HELLO, DATABEND!          │
└───────────────────────────────────────────────────────┘
```
