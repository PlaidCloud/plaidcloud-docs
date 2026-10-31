---
title: TRANSLATE (Lakehouse v1)
description: TRANSLATE transforme une chaîne donnée en remplaçant des caractères précis par les caractères correspondants.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/translate.md
---

Transforme une chaîne donnée en remplaçant des caractères précis par les caractères de remplacement correspondants, selon la correspondance fournie.

## Syntaxe Analyze

```python
func.translate('<inputString>', '<charactersToReplace>', '<replacementCharacters>')
```

## Exemples Analyze

```python
func.translate('databend', 'de', 'DE')
┌────────────────────────────────────────┐
│ func.translate('databend', 'de', 'DE') │
├────────────────────────────────────────┤
│ DatabEnD                               │
└────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TRANSLATE('<inputString>', '<charactersToReplace>', '<replacementCharacters>')
```

| Paramètre                 | Description                                                                                                         |
|---------------------------|---------------------------------------------------------------------------------------------------------------------|
| `<inputString>`           | La chaîne d'entrée à transformer.                                                                                   |
| `<charactersToReplace>`   | La chaîne contenant les caractères à remplacer dans la chaîne d'entrée.                                             |
| `<replacementCharacters>` | La chaîne contenant les caractères de remplacement correspondant à ceux de `<charactersToReplace>`.                 |

## Exemples SQL

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
