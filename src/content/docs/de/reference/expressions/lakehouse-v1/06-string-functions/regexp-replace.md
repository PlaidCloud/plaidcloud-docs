---
title: REGEXP_REPLACE (Lakehouse v1)
description: REGEXP_REPLACE – ersetzt Vorkommen in der Zeichenfolge expr, die zum regulären Ausdruck passen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-replace.md
---

Ersetzt Vorkommen in der Zeichenfolge `expr`, die zum durch das Muster `pat` angegebenen regulären Ausdruck passen, durch die Ersetzungszeichenfolge `repl` und gibt die resultierende Zeichenfolge zurück. Ist `expr`, `pat` oder `repl` NULL, ist der Rückgabewert NULL.

## Analyze-Syntax

```python
func.regexp_replace(<expr>, <pat>, <repl[, pos[, occurrence[, match_type]]]>)
```

## Analyze-Beispiele

```python
func.regexp_replace('a b c', 'b', 'X')
┌────────────────────────────────────────┐
│ func.regexp_replace('a b c', 'b', 'X') │
├────────────────────────────────────────┤
│ a X c                                  │
└────────────────────────────────────────┘
```

## SQL-Syntax

```sql
REGEXP_REPLACE(<expr>, <pat>, <repl[, pos[, occurrence[, match_type]]]>)
```

## Argumente

| Argumente  | Beschreibung                                                                                                                         |
|------------|--------------------------------------------------------------------------------------------------------------------------------------|
| expr       | Die Zeichenfolge expr, auf die das Muster angewendet wird                                                                            |
| pat        | Der reguläre Ausdruck                                                                                                                |
| repl       | Die Ersetzungszeichenfolge                                                                                                           |
| pos        | Optional. Die Position in expr, an der die Suche beginnt. Wenn nicht angegeben, ist der Standardwert 1.                              |
| occurrence | Optional. Welches Vorkommen einer Übereinstimmung ersetzt wird. Wenn nicht angegeben, ist der Standardwert 0 (das heißt „alle Vorkommen ersetzen“). |
| match_type | Optional. Eine Zeichenfolge, die angibt, wie der Abgleich durchgeführt wird. Die Bedeutung entspricht der Beschreibung für REGEXP_LIKE(). |

## Rückgabetyp

`VARCHAR`

## SQL-Beispiele

```sql
SELECT REGEXP_REPLACE('a b c', 'b', 'X');
┌───────────────────────────────────┐
│ REGEXP_REPLACE('a b c', 'b', 'X') │
├───────────────────────────────────┤
│ a X c                             │
└───────────────────────────────────┘

SELECT REGEXP_REPLACE('abc def ghi', '[a-z]+', 'X', 1, 3);
┌────────────────────────────────────────────────────┐
│ REGEXP_REPLACE('abc def ghi', '[a-z]+', 'X', 1, 3) │
├────────────────────────────────────────────────────┤
│ abc def X                                          │
└────────────────────────────────────────────────────┘

SELECT REGEXP_REPLACE('周 周周 周周周', '周+', 'X', 3, 2);
┌───────────────────────────────────────────────────────────┐
│ REGEXP_REPLACE('周 周周 周周周', '周+', 'X', 3, 2)        │
├───────────────────────────────────────────────────────────┤
│ 周 周周 X                                                 │
└───────────────────────────────────────────────────────────┘
```
