---
title: TRANSLATE (Lakehouse v1)
description: TRANSLATE — transforma uma string substituindo caracteres específicos pelos caracteres correspondentes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/translate.md
---

Transforma uma string substituindo caracteres específicos pelas substituições correspondentes, conforme definido pelo mapeamento fornecido.

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

| Parâmetro                 | Descrição                                                                                                  |
|---------------------------|------------------------------------------------------------------------------------------------------------|
| `<inputString>`           | A string de entrada a ser transformada.                                                                    |
| `<charactersToReplace>`   | A string que contém os caracteres a serem substituídos na string de entrada.                               |
| `<replacementCharacters>` | A string que contém os caracteres de substituição correspondentes aos de `<charactersToReplace>`.          |

## Exemplos de SQL

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
