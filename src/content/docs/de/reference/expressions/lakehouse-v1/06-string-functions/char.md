---
title: CHAR (Lakehouse v1)
description: CHAR – gibt für jede übergebene Ganzzahl das entsprechende Zeichen zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/char.md
---

Gibt für jede übergebene Ganzzahl das entsprechende Zeichen zurück.

## Analyze-Syntax

```python
func.char(N,...)
```

## Analyze-Beispiele

```python
func.char(77,121,83,81,76)
┌─────────────────────────────┐
│ func.char(77,121,83,81,76) │
├─────────────────────────────┤
│ 4D7953514C                  │
└─────────────────────────────┘
```

## SQL-Syntax

```sql
CHAR(N, ...)
```

## Argumente

| Argumente | Beschreibung       |
|-----------|--------------------|
| N         | Numerische Spalte  |

## Rückgabetyp

`BINARY`

## SQL-Beispiele

Dieses Beispiel zeigt sowohl den zurückgegebenen Binärwert als auch die Zeichenfolgendarstellung.

```sql
SELECT CHAR(77,121,83,81,76) as a, a::String;
┌────────────────────────┐
│      a     │ a::string │
│   Binary   │   String  │
├────────────┼───────────┤
│ 4D7953514C │ MySQL     │
└────────────────────────┘
```
