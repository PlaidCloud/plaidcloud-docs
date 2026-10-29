---
title: REGEXP_SUBSTR (Lakehouse v1)
description: REGEXP_SUBSTR – gibt die Teilzeichenfolge der Zeichenfolge expr zurück, die zum regulären Ausdruck passt.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-substr.md
---

Gibt die Teilzeichenfolge der Zeichenfolge `expr` zurück, die zum durch das Muster `pat` angegebenen regulären Ausdruck passt, oder NULL, wenn es keine Übereinstimmung gibt. Ist expr oder pat NULL, ist der Rückgabewert NULL.

## Analyze-Syntax

```python
func.regexp_substr(<expr>, <pat[, pos[, occurrence[, match_type]]]>)
```

## Analyze-Beispiele

```python
func.regexp_substr('abc def ghi', '[a-z]+')
┌─────────────────────────────────────────────┐
│ func.regexp_substr('abc def ghi', '[a-z]+') │
├─────────────────────────────────────────────┤
│ abc                                         │
└─────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
REGEXP_SUBSTR(<expr>, <pat[, pos[, occurrence[, match_type]]]>)
```

## Argumente

| Argumente  | Beschreibung                                                                                                                         |
|------------|--------------------------------------------------------------------------------------------------------------------------------------|
| expr       | Die Zeichenfolge expr, auf die das Muster angewendet wird                                                                            |
| pat        | Der reguläre Ausdruck                                                                                                                |
| pos        | Optional. Die Position in expr, an der die Suche beginnt. Wenn nicht angegeben, ist der Standardwert 1.                              |
| occurrence | Optional. Nach welchem Vorkommen einer Übereinstimmung gesucht wird. Wenn nicht angegeben, ist der Standardwert 1.                   |
| match_type | Optional. Eine Zeichenfolge, die angibt, wie der Abgleich durchgeführt wird. Die Bedeutung entspricht der Beschreibung für REGEXP_LIKE(). |

## Rückgabetyp

`VARCHAR`

## SQL-Beispiele

```sql
SELECT REGEXP_SUBSTR('abc def ghi', '[a-z]+');
┌────────────────────────────────────────┐
│ REGEXP_SUBSTR('abc def ghi', '[a-z]+') │
├────────────────────────────────────────┤
│ abc                                    │
└────────────────────────────────────────┘

SELECT REGEXP_SUBSTR('abc def ghi', '[a-z]+', 1, 3);
┌──────────────────────────────────────────────┐
│ REGEXP_SUBSTR('abc def ghi', '[a-z]+', 1, 3) │
├──────────────────────────────────────────────┤
│ ghi                                          │
└──────────────────────────────────────────────┘

SELECT REGEXP_SUBSTR('周 周周 周周周 周周周周', '周+', 2, 3);
┌──────────────────────────────────────────────────────────────────┐
│ REGEXP_SUBSTR('周 周周 周周周 周周周周', '周+', 2, 3)            │
├──────────────────────────────────────────────────────────────────┤
│ 周周周周                                                         │
└──────────────────────────────────────────────────────────────────┘

```
