---
title: REGEXP_INSTR (Lakehouse v1)
description: REGEXP_INSTR – gibt den Startindex der Teilzeichenfolge von expr zurück, die zum durch das Muster pat angegebenen regulären Ausdruck passt, oder 0, wenn es keine Übereinstimmung gibt.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-instr.md
---

Gibt den Startindex der Teilzeichenfolge der Zeichenfolge `expr` zurück, die zum durch das Muster `pat` angegebenen regulären Ausdruck passt, oder `0`, wenn es keine Übereinstimmung gibt. Ist `expr` oder `pat` NULL, ist der Rückgabewert NULL. Zeichenindizes beginnen bei `1`.

## Analyze-Syntax

```python
func.regexp_instr(<expr>, <pat[, pos[, occurrence[, return_option[, match_type]]]]>)
```

## Analyze-Beispiele

```python
func.regexp_instr('dog cat dog', 'dog')
┌─────────────────────────────────────────┐
│ func.regexp_instr('dog cat dog', 'dog') │
├─────────────────────────────────────────┤
│                                       1 │
└─────────────────────────────────────────┘
```

## SQL-Syntax

```sql
REGEXP_INSTR(<expr>, <pat[, pos[, occurrence[, return_option[, match_type]]]]>)
```

## Argumente

| Argumente     | Beschreibung                                                                                                                                                                                                                                                                                             |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| expr          | Die Zeichenfolge expr, auf die das Muster angewendet wird                                                                                                                                                                                                                                                |
| pat           | Der reguläre Ausdruck                                                                                                                                                                                                                                                                                    |
| pos           | Optional. Die Position in expr, an der die Suche beginnt. Wenn nicht angegeben, ist der Standardwert 1.                                                                                                                                                                                                  |
| occurrence    | Optional. Nach welchem Vorkommen einer Übereinstimmung gesucht wird. Wenn nicht angegeben, ist der Standardwert 1.                                                                                                                                                                                       |
| return_option | Optional. Welche Art von Position zurückgegeben wird. Bei 0 gibt REGEXP_INSTR() die Position des ersten Zeichens der übereinstimmenden Teilzeichenfolge zurück. Bei 1 gibt REGEXP_INSTR() die Position nach der übereinstimmenden Teilzeichenfolge zurück. Wenn nicht angegeben, ist der Standardwert 0. |
| match_type    | Optional. Eine Zeichenfolge, die angibt, wie der Abgleich durchgeführt wird. Die Bedeutung entspricht der Beschreibung für REGEXP_LIKE().                                                                                                                                                                 |

## Rückgabetyp

Ein Wert eines numerischen Datentyps.

## SQL-Beispiele

```sql
SELECT REGEXP_INSTR('dog cat dog', 'dog');
┌────────────────────────────────────┐
│ REGEXP_INSTR('dog cat dog', 'dog') │
├────────────────────────────────────┤
│                                  1 │
└────────────────────────────────────┘

SELECT REGEXP_INSTR('dog cat dog', 'dog', 2);
┌───────────────────────────────────────┐
│ REGEXP_INSTR('dog cat dog', 'dog', 2) │
├───────────────────────────────────────┤
│                                     9 │
└───────────────────────────────────────┘

SELECT REGEXP_INSTR('aa aaa aaaa', 'a{2}');
┌─────────────────────────────────────┐
│ REGEXP_INSTR('aa aaa aaaa', 'a{2}') │
├─────────────────────────────────────┤
│                                   1 │
└─────────────────────────────────────┘

SELECT REGEXP_INSTR('aa aaa aaaa', 'a{4}');
┌─────────────────────────────────────┐
│ REGEXP_INSTR('aa aaa aaaa', 'a{4}') │
├─────────────────────────────────────┤
│                                   8 │
└─────────────────────────────────────┘
```
