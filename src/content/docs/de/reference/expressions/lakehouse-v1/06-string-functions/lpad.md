---
title: LPAD (Lakehouse v1)
description: LPAD – gibt die Zeichenfolge str zurück, links mit der Zeichenfolge padstr auf eine Länge von len Zeichen aufgefüllt.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/lpad.md
---

Gibt die Zeichenfolge str zurück, links mit der Zeichenfolge padstr auf eine Länge von len Zeichen aufgefüllt.
Ist str länger als len, wird der Rückgabewert auf len Zeichen gekürzt.

## Analyze-Syntax

```python
func.lpad(<str>, <len>, <padstr>)
```

## Analyze-Beispiele

```python
func.lpad('hi',4,'??')
┌────────────────────────┐
│ func.lpad('hi',4,'??') │
├────────────────────────┤
│ ??hi                   │
└────────────────────────┘
```

```python
func.lpad('hi',1,'??')
┌────────────────────────┐
│ func.lpad('hi',1,'??') │
├────────────────────────┤
│ h                      │
└────────────────────────┘
```

## SQL-Syntax

```sql
LPAD(<str>, <len>, <padstr>)
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
SELECT LPAD('hi',4,'??');
┌─────────────────────┐
│ LPAD('hi', 4, '??') │
├─────────────────────┤
│ ??hi                │
└─────────────────────┘

SELECT LPAD('hi',1,'??');
┌─────────────────────┐
│ LPAD('hi', 1, '??') │
├─────────────────────┤
│ h                   │
└─────────────────────┘
```
