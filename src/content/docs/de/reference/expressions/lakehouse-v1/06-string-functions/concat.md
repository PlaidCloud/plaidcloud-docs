---
title: CONCAT (Lakehouse v1)
description: CONCAT – gibt die Zeichenfolge zurück, die sich aus der Verkettung der Argumente ergibt.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/concat.md
---

Gibt die Zeichenfolge zurück, die sich aus der Verkettung der Argumente ergibt. Die Funktion kann ein oder mehrere Argumente haben. Sind alle Argumente nicht binäre Zeichenfolgen, ist das Ergebnis eine nicht binäre Zeichenfolge. Enthalten die Argumente binäre Zeichenfolgen, ist das Ergebnis eine binäre Zeichenfolge. Ein numerisches Argument wird in die entsprechende nicht binäre Zeichenfolgenform umgewandelt.

## Analyze-Syntax

```python
func.concat(<expr1>, ...)
```

## Analyze-Beispiele

```python
func.concat('data', 'bend')
┌─────────────────────────────┐
│ func.concat('data', 'bend') │
├─────────────────────────────┤
│ databend                    │
└─────────────────────────────┘
```

## SQL-Syntax

```sql
CONCAT(<expr1>, ...)
```

## Argumente

| Argumente | Beschreibung |
|-----------|--------------|
| `<expr1>` | Zeichenfolge |

## Rückgabetyp

Ein Wert vom Datentyp `VARCHAR` oder vom Datentyp `NULL`.

## SQL-Beispiele

```sql
SELECT CONCAT('data', 'bend');
┌────────────────────────┐
│ concat('data', 'bend') │
├────────────────────────┤
│ databend               │
└────────────────────────┘

SELECT CONCAT('data', NULL, 'bend');
┌──────────────────────────────┐
│ CONCAT('data', NULL, 'bend') │
├──────────────────────────────┤
│                         NULL │
└──────────────────────────────┘

SELECT CONCAT('14.3');
┌────────────────┐
│ concat('14.3') │
├────────────────┤
│ 14.3           │
└────────────────┘
```
