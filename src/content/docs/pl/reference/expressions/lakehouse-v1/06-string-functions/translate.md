---
title: TRANSLATE (Lakehouse v1)
description: TRANSLATE — przekształca podany ciąg znaków, zastępując wybrane znaki odpowiadającymi im zamiennikami.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/translate.md
---

Przekształca podany ciąg znaków, zastępując wybrane znaki odpowiadającymi im zamiennikami, zgodnie z podanym odwzorowaniem.

## Składnia Analyze

```python
func.translate('<inputString>', '<charactersToReplace>', '<replacementCharacters>')
```

## Przykłady Analyze

```python
func.translate('databend', 'de', 'DE')
┌────────────────────────────────────────┐
│ func.translate('databend', 'de', 'DE') │
├────────────────────────────────────────┤
│ DatabEnD                               │
└────────────────────────────────────────┘
```

## Składnia SQL

```sql
TRANSLATE('<inputString>', '<charactersToReplace>', '<replacementCharacters>')
```

| Parametr                  | Opis                                                                                                     |
|---------------------------|----------------------------------------------------------------------------------------------------------|
| `<inputString>`           | Wejściowy ciąg znaków do przekształcenia.                                                                |
| `<charactersToReplace>`   | Ciąg zawierający znaki, które mają zostać zastąpione w ciągu wejściowym.                                 |
| `<replacementCharacters>` | Ciąg zawierający znaki zastępujące, odpowiadające znakom z `<charactersToReplace>`.                      |

## Przykłady SQL

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
