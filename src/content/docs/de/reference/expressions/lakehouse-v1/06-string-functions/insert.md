---
title: INSERT (Lakehouse v1)
description: INSERT – gibt die Zeichenfolge str zurück, in der die ab Position pos beginnende Teilzeichenfolge der Länge len ersetzt wurde.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/insert.md
---

Gibt die Zeichenfolge str zurück, in der die ab Position pos beginnende Teilzeichenfolge mit einer Länge von len Zeichen durch die Zeichenfolge newstr ersetzt wurde. Liegt pos nicht innerhalb der Länge der Zeichenfolge, wird die ursprüngliche Zeichenfolge zurückgegeben. Liegt len nicht innerhalb der Länge des Rests der Zeichenfolge, wird der Rest der Zeichenfolge ab Position pos ersetzt. Gibt NULL zurück, wenn ein Argument NULL ist.

## Analyze-Syntax

```python
func.insert(<str>, <pos>, <len>, <newstr>)
```

## Analyze-Beispiele

```python
func.insert('Quadratic', 3, 4, 'What')
┌────────────────────────────────────────┐
│ func.insert('Quadratic', 3, 4, 'What') │
├────────────────────────────────────────┤
│ QuWhattic                              │
└────────────────────────────────────────┘
```

## SQL-Syntax

```sql
INSERT(<str>, <pos>, <len>, <newstr>)
```

## Argumente

| Argumente  | Beschreibung              |
|------------|---------------------------|
| `<str>`    | Die Zeichenfolge.         |
| `<pos>`    | Die Position.             |
| `<len>`    | Die Länge.                |
| `<newstr>` | Die neue Zeichenfolge.    |

## Rückgabetyp

`VARCHAR`

## SQL-Beispiele

```sql
SELECT INSERT('Quadratic', 3, 4, 'What');
┌───────────────────────────────────┐
│ INSERT('Quadratic', 3, 4, 'What') │
├───────────────────────────────────┤
│ QuWhattic                         │
└───────────────────────────────────┘

SELECT INSERT('Quadratic', -1, 4, 'What');
┌───────────────────────────────────────┐
│ INSERT('Quadratic', (- 1), 4, 'What') │
├───────────────────────────────────────┤
│ Quadratic                             │
└───────────────────────────────────────┘

SELECT INSERT('Quadratic', 3, 100, 'What');
┌─────────────────────────────────────┐
│ INSERT('Quadratic', 3, 100, 'What') │
├─────────────────────────────────────┤
│ QuWhat                              │
└─────────────────────────────────────┘

┌────────────────────────────────────────────┬────────┐
│ INSERT('123456789', number, number, 'aaa') │ number │
├────────────────────────────────────────────┼────────┤
│ 123456789                                  │      0 │
│ aaa23456789                                │      1 │
│ 1aaa456789                                 │      2 │
│ 12aaa6789                                  │      3 │
│ 123aaa89                                   │      4 │
│ 1234aaa                                    │      5 │
│ 12345aaa                                   │      6 │
│ 123456aaa                                  │      7 │
│ 1234567aaa                                 │      8 │
│ 12345678aaa                                │      9 │
│ 123456789                                  │     10 │
│ 123456789                                  │     11 │
│ 123456789                                  │     12 │
└────────────────────────────────────────────┴────────┘
```
