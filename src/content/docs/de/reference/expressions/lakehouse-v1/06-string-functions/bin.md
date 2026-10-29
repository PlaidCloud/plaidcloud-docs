---
title: BIN (Lakehouse v1)
description: BIN – gibt eine Zeichenfolgendarstellung des Binärwerts von N zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/bin.md
---

Gibt eine Zeichenfolgendarstellung des Binärwerts von N zurück.

## Analyze-Syntax

```python
func.bin(<expr>)
```

## Analyze-Beispiele

```python
func.bin(12)
┌──────────────┐
│ func.bin(12) │
├──────────────┤
│ 1100         │
└──────────────┘
```

## SQL-Syntax

```sql
BIN(<expr>)
```

## Argumente

| Argumente | Beschreibung |
|-----------|--------------|
| `<expr>`  | Die Zahl.    |

## Rückgabetyp

`VARCHAR`

## SQL-Beispiele

```sql
SELECT BIN(12);
┌─────────┐
│ BIN(12) │
├─────────┤
│ 1100    │
└─────────┘
```
