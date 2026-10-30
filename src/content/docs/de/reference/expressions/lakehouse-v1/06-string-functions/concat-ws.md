---
title: CONCAT_WS (Lakehouse v1)
description: CONCAT_WS – CONCAT_WS() steht für „Concatenate With Separator“ (mit Trennzeichen verketten) und ist eine Sonderform von CONCAT().
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/concat-ws.md
---

CONCAT_WS() steht für „Concatenate With Separator“ (mit Trennzeichen verketten) und ist eine Sonderform von CONCAT(). Das erste Argument ist das Trennzeichen für die übrigen Argumente. Das Trennzeichen wird zwischen die zu verkettenden Zeichenfolgen eingefügt. Das Trennzeichen kann eine Zeichenfolge sein, ebenso wie die übrigen Argumente. Ist das Trennzeichen NULL, ist das Ergebnis NULL.

CONCAT_WS() überspringt leere Zeichenfolgen nicht. NULL-Werte nach dem Trennzeichen-Argument überspringt die Funktion jedoch.

## Analyze-Syntax

```python
func.concat_ws(<separator>, <expr1>, ...)
```

## Analyze-Beispiele

```python
func.concat_ws(',', 'data', 'fuse', 'labs', '2021')
┌─────────────────────────────────────────────────────┐
│ func.concat_ws(',', 'data', 'fuse', 'labs', '2021') │
├─────────────────────────────────────────────────────┤
│ data,fuse,labs,2021                                 │
└─────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
CONCAT_WS(<separator>, <expr1>, ...)
```

## Argumente

| Argumente     | Beschreibung       |
|---------------| ------------------ |
| `<separator>` | Zeichenfolgenspalte |
| `<expr1>`     | Wertspalte         |

## Rückgabetyp

Ein Wert vom Datentyp `VARCHAR` oder vom Datentyp `NULL`.

## SQL-Beispiele

```sql
SELECT CONCAT_WS(',', 'data', 'fuse', 'labs', '2021');
┌────────────────────────────────────────────────┐
│ CONCAT_WS(',', 'data', 'fuse', 'labs', '2021') │
├────────────────────────────────────────────────┤
│ data,fuse,labs,2021                            │
└────────────────────────────────────────────────┘

SELECT CONCAT_WS(',', 'data', NULL, 'bend');
┌──────────────────────────────────────┐
│ CONCAT_WS(',', 'data', NULL, 'bend') │
├──────────────────────────────────────┤
│ data,bend                            │
└──────────────────────────────────────┘


SELECT CONCAT_WS(',', 'data', NULL, NULL, 'bend');
┌────────────────────────────────────────────┐
│ CONCAT_WS(',', 'data', NULL, NULL, 'bend') │
├────────────────────────────────────────────┤
│ data,bend                                  │
└────────────────────────────────────────────┘


SELECT CONCAT_WS(NULL, 'data', 'fuse', 'labs');
┌─────────────────────────────────────────┐
│ CONCAT_WS(NULL, 'data', 'fuse', 'labs') │
├─────────────────────────────────────────┤
│                                    NULL │
└─────────────────────────────────────────┘

SELECT CONCAT_WS(',', NULL);
┌──────────────────────┐
│ CONCAT_WS(',', NULL) │
├──────────────────────┤
│                      │
└──────────────────────┘
```
