---
title: REGEXP_LIKE (Lakehouse v1)
description: REGEXP_LIKE – prüft, ob die Zeichenfolge zum regulären Ausdruck passt.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-like.md
---

Die Funktion REGEXP_LIKE prüft, ob die Zeichenfolge zum regulären Ausdruck passt.

## Analyze-Syntax

```python
func.regexp_like(<expr>, <pat[, match_type]>)
```

## Analyze-Beispiele

```python
func.regexp_like('a', '^[a-d]')
┌─────────────────────────────────┐
│ func.regexp_like('a', '^[a-d]') │
├─────────────────────────────────┤
│                               1 │
└─────────────────────────────────┘
```

## SQL-Syntax

```sql
REGEXP_LIKE(<expr>, <pat[, match_type]>)
```

## Argumente

| Argumente      | Beschreibung                                                                                |
|----------------|---------------------------------------------------------------------------------------------|
| `<expr>`       | Die Zeichenfolge expr, auf die das Muster angewendet wird                                   |
| `<pat>`        | Der reguläre Ausdruck                                                                       |
| `[match_type]` | Optional. Das Argument match_type ist eine Zeichenfolge, die angibt, wie der Abgleich erfolgt |

`match_type` kann eines oder alle der folgenden Zeichen enthalten:

* `c`: Abgleich unter Beachtung der Groß-/Kleinschreibung.
* `i`: Abgleich ohne Beachtung der Groß-/Kleinschreibung.
* `m`: Mehrzeilenmodus. Zeilenumbrüche innerhalb der Zeichenfolge werden erkannt. Standardmäßig werden Zeilenumbrüche nur am Anfang und am Ende des Zeichenfolgenausdrucks abgeglichen.
* `n`: Das Zeichen `.` stimmt mit Zeilenumbrüchen überein. Standardmäßig endet der Abgleich mit `.` am Zeilenende.
* `u`: Nur Unix-Zeilenenden. Wird derzeit nicht unterstützt.

## Rückgabetyp

`BIGINT`
Gibt `1` zurück, wenn die Zeichenfolge expr zum durch das Muster pat angegebenen regulären Ausdruck passt, andernfalls `0`. Ist expr oder pat NULL, ist der Rückgabewert NULL.

## SQL-Beispiele

```sql
SELECT REGEXP_LIKE('a', '^[a-d]');
┌────────────────────────────┐
│ REGEXP_LIKE('a', '^[a-d]') │
├────────────────────────────┤
│                          1 │
└────────────────────────────┘

SELECT REGEXP_LIKE('abc', 'ABC');
┌───────────────────────────┐
│ REGEXP_LIKE('abc', 'ABC') │
├───────────────────────────┤
│                         1 │
└───────────────────────────┘

SELECT REGEXP_LIKE('abc', 'ABC', 'c');
┌────────────────────────────────┐
│ REGEXP_LIKE('abc', 'ABC', 'c') │
├────────────────────────────────┤
│                              0 │
└────────────────────────────────┘

SELECT REGEXP_LIKE('new*\n*line', 'new\\*.\\*line');

┌───────────────────────────────────────────┐
│ REGEXP_LIKE('new*\n*line', 'new\*.\*line')│
├───────────────────────────────────────────┤
│                                         0 │
└───────────────────────────────────────────┘

SELECT REGEXP_LIKE('new*\n*line', 'new\\*.\\*line', 'n');

┌────────────────────────────────────────────────┐
│ REGEXP_LIKE('new*\n*line', 'new\*.\*line', 'n')│
├────────────────────────────────────────────────┤
│                                              1 │
└────────────────────────────────────────────────┘
```
