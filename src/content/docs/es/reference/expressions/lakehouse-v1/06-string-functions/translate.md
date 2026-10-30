---
title: TRANSLATE (Lakehouse v1)
description: TRANSLATE — transforma una cadena dada reemplazando caracteres específicos por los reemplazos correspondientes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/translate.md
---

Transforma una cadena dada reemplazando caracteres específicos por los reemplazos correspondientes, según la asignación proporcionada.

## Sintaxis de Analyze

```python
func.translate('<inputString>', '<charactersToReplace>', '<replacementCharacters>')
```

## Ejemplos de Analyze

```python
func.translate('databend', 'de', 'DE')
┌────────────────────────────────────────┐
│ func.translate('databend', 'de', 'DE') │
├────────────────────────────────────────┤
│ DatabEnD                               │
└────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
TRANSLATE('<inputString>', '<charactersToReplace>', '<replacementCharacters>')
```

| Parámetro                 | Descripción                                                                                     |
|---------------------------|-------------------------------------------------------------------------------------------------|
| `<inputString>`           | La cadena de entrada que se va a transformar.                                                   |
| `<charactersToReplace>`   | La cadena que contiene los caracteres que se van a reemplazar en la cadena de entrada.          |
| `<replacementCharacters>` | La cadena que contiene los caracteres de reemplazo correspondientes a los de `<charactersToReplace>`. |

## Ejemplos de SQL

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
