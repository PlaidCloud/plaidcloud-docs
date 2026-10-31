---
title: SUBSTR (Lakehouse v1)
description: SUBSTR – extrahiert ab einer bestimmten Position eine Zeichenfolge mit einer bestimmten Anzahl von Zeichen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/substr.md
---

Extrahiert ab einer bestimmten Position einer angegebenen Zeichenfolge eine Zeichenfolge mit einer bestimmten Anzahl von Zeichen.

- Die Formen ohne Argument `len` geben eine Teilzeichenfolge der Zeichenfolge `str` ab Position `pos` zurück.
- Die Formen mit Argument `len` geben eine Teilzeichenfolge der Länge `len` Zeichen aus der Zeichenfolge `str` zurück, beginnend bei Position `pos`.

Für `pos` kann auch ein negativer Wert verwendet werden. In diesem Fall liegt der Beginn der Teilzeichenfolge pos Zeichen vom Ende der Zeichenfolge entfernt statt vom Anfang. Ein negativer Wert für `pos` ist in allen Formen dieser Funktion zulässig. Ein Wert von 0 für `pos` gibt eine leere Zeichenfolge zurück. Die Position des ersten Zeichens der Zeichenfolge, aus der die Teilzeichenfolge extrahiert werden soll, zählt als 1.

## Analyze-Syntax

```python
func.substr(<str>, <pos>, <len>)
```

## Analyze-Beispiele

```python
func.substr('Quadratically', 5, 6)
┌────────────────────────────────────┐
│ func.substr('Quadratically', 5, 6) │
├────────────────────────────────────┤
│ ratica                             │
└────────────────────────────────────┘
```

## SQL-Syntax

```sql
SUBSTR(<str>, <pos>)

SUBSTR(<str>, <pos>, <len>)
```

## Argumente

| Argumente | Beschreibung                                                                                                   |
|-----------|----------------------------------------------------------------------------------------------------------------|
| `<str>`   | Die Hauptzeichenfolge, aus der die Zeichen extrahiert werden                                                   |
| `<pos>`   | Die Position (ab 1), an der die Teilzeichenfolge beginnt. Bei einem negativen Wert wird vom Ende aus gezählt   |
| `<len>`   | Die maximale Länge der zu extrahierenden Teilzeichenfolge                                                      |

## Aliase

- [SUBSTRING](../substring)
- [MID](../mid)

## Rückgabetyp

VARCHAR

## SQL-Beispiele

```sql
SELECT
  SUBSTRING('Quadratically', 5),
  SUBSTR('Quadratically', 5),
  MID('Quadratically', 5);

┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│ substring('quadratically' from 5) │ substring('quadratically' from 5) │ mid('quadratically', 5) │
├───────────────────────────────────┼───────────────────────────────────┼─────────────────────────┤
│ ratically                         │ ratically                         │ ratically               │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘

SELECT
  SUBSTRING('Quadratically', 5, 6),
  SUBSTR('Quadratically', 5, 6),
  MID('Quadratically', 5, 6);

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ substring('quadratically' from 5 for 6) │ substring('quadratically' from 5 for 6) │ mid('quadratically', 5, 6) │
├─────────────────────────────────────────┼─────────────────────────────────────────┼────────────────────────────┤
│ ratica                                  │ ratica                                  │ ratica                     │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
