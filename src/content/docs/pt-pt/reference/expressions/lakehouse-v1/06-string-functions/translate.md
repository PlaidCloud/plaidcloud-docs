---
title: TRANSLATE (Lakehouse v1)
description: TRANSLATE — transforma uma cadeia de caracteres substituindo determinados caracteres pelos caracteres correspondentes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/translate.md
---

Transforma uma cadeia de caracteres substituindo determinados caracteres pelas substituições correspondentes, conforme definido pelo mapeamento fornecido.

## Sintaxe do Analyze

```python
func.translate('<inputString>', '<charactersToReplace>', '<replacementCharacters>')
```

## Exemplos do Analyze

```python
func.translate('databend', 'de', 'DE')
┌────────────────────────────────────────┐
│ func.translate('databend', 'de', 'DE') │
├────────────────────────────────────────┤
│ DatabEnD                               │
└────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TRANSLATE('<inputString>', '<charactersToReplace>', '<replacementCharacters>')
```

| Parâmetro                 | Descrição                                                                                                     |
|---------------------------|---------------------------------------------------------------------------------------------------------------|
| `<inputString>`           | A cadeia de caracteres de entrada a transformar.                                                              |
| `<charactersToReplace>`   | A cadeia de caracteres que contém os caracteres a substituir na cadeia de entrada.                            |
| `<replacementCharacters>` | A cadeia de caracteres que contém os caracteres de substituição correspondentes aos de `<charactersToReplace>`. |

## Exemplos SQL

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
