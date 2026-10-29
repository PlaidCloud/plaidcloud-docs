---
title: REPLACE (Lakehouse v1)
description: REPLACE – gibt die Zeichenfolge str zurück, in der alle Vorkommen der Zeichenfolge from_str durch die Zeichenfolge to_str ersetzt wurden.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/replace.md
---

Gibt die Zeichenfolge str zurück, in der alle Vorkommen der Zeichenfolge from_str durch die Zeichenfolge to_str ersetzt wurden.

## Analyze-Syntax

```python
func.replace(<str>, <from_str>, <to_str>)
```

## Analyze-Beispiele

```python
func.replace(<str>, <from_str>, <to_str>)
┌──────────────────────────────────────┐
│ func.replace('plaidCloud', 'p', 'P') │
├──────────────────────────────────────┤
│ PlaidCloud                           │
└──────────────────────────────────────┘
```

## SQL-Syntax

```sql
REPLACE(<str>, <from_str>, <to_str>)
```

## Argumente

| Argumente    | Beschreibung                  |
|--------------|-------------------------------|
| `<str>`      | Die Zeichenfolge.             |
| `<from_str>` | Die zu ersetzende Zeichenfolge. |
| `<to_str>`   | Die Ersatzzeichenfolge.       |

## Rückgabetyp

`VARCHAR`

## SQL-Beispiele

```sql
SELECT REPLACE('www.mysql.com', 'w', 'Ww');
┌─────────────────────────────────────┐
│ REPLACE('www.mysql.com', 'w', 'Ww') │
├─────────────────────────────────────┤
│ WwWwWw.mysql.com                    │
└─────────────────────────────────────┘
```
