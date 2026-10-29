---
title: TRANSLATE (Lakehouse v1)
description: TRANSLATE – wandelt eine Zeichenfolge um, indem bestimmte Zeichen durch entsprechende Ersatzzeichen ersetzt werden.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/translate.md
---

Wandelt eine angegebene Zeichenfolge um, indem bestimmte Zeichen gemäß der angegebenen Zuordnung durch entsprechende Ersatzzeichen ersetzt werden.

## Analyze-Syntax

```python
func.translate('<inputString>', '<charactersToReplace>', '<replacementCharacters>')
```

## Analyze-Beispiele

```python
func.translate('databend', 'de', 'DE')
┌────────────────────────────────────────┐
│ func.translate('databend', 'de', 'DE') │
├────────────────────────────────────────┤
│ DatabEnD                               │
└────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TRANSLATE('<inputString>', '<charactersToReplace>', '<replacementCharacters>')
```

| Parameter                 | Beschreibung                                                                                                          |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `<inputString>`           | Die umzuwandelnde Eingabezeichenfolge.                                                                                |
| `<charactersToReplace>`   | Die Zeichenfolge mit den Zeichen, die in der Eingabezeichenfolge ersetzt werden sollen.                               |
| `<replacementCharacters>` | Die Zeichenfolge mit den Ersatzzeichen, die den Zeichen in `<charactersToReplace>` entsprechen.                       |

## SQL-Beispiele

```sql
-- Replace 'd' with '$' in 'databend'
SELECT TRANSLATE('databend', 'd', '$');

---
$ataben$

-- Replace 'd' with 'D' in 'databend'
SELECT TRANSLATE('databend', 'd', 'D');

---
DatabenD

-- Replace 'd' with 'D' and 'e' with 'E' in 'databend'
SELECT TRANSLATE('databend', 'de', 'DE');

---
DatabEnD

-- Remove 'd' from 'databend'
SELECT TRANSLATE('databend', 'd', '');

---
ataben
```
