---
title: RPAD (Lakehouse v1)
description: RPAD – gibt die Zeichenfolge str zurück, rechts mit der Zeichenfolge padstr auf eine Länge von len Zeichen aufgefüllt.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/rpad.md
---

Gibt die Zeichenfolge str zurück, rechts mit der Zeichenfolge padstr auf eine Länge von len Zeichen aufgefüllt.
Ist str länger als len, wird der Rückgabewert auf len Zeichen gekürzt.

## Analyze-Syntax

```python
func.rpad(<str>, <len>, <padstr>)
```

## Analyze-Beispiele

```python
func.rpad('hi',5,'?')
┌───────────────────────┐
│ func.rpad('hi',5,'?') │
├───────────────────────┤
│ hi???                 │
└───────────────────────┘

func.rpad('hi',1,'?')
┌───────────────────────┐
│ func.rpad('hi',1,'?') │
├───────────────────────┤
│ h                     │
└───────────────────────┘
```

## SQL-Syntax

```sql
RPAD(<str>, <len>, <padstr>)
```

## Argumente

| Argumente  | Beschreibung               |
|------------|----------------------------|
| `<str>`    | Die Zeichenfolge.          |
| `<len>`    | Die Länge.                 |
| `<padstr>` | Die Auffüllzeichenfolge.   |

## Rückgabetyp

`VARCHAR`

## SQL-Beispiele

```sql
SELECT RPAD('hi',5,'?');
┌────────────────────┐
│ RPAD('hi', 5, '?') │
├────────────────────┤
│ hi???              │
└────────────────────┘

SELECT RPAD('hi',1,'?');
┌────────────────────┐
│ RPAD('hi', 1, '?') │
├────────────────────┤
│ h                  │
└────────────────────┘
```
