---
title: TOKENIZE (Lakehouse v2)
description: "Use la función de cadena TOKENIZE en PlaidCloud Lakehouse. Divide una cadena en una matriz de términos mediante el analizador especificado. Es útil en escenarios de búsqueda de texto completo."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/tokenize.md
---

Divide una cadena en una matriz de términos mediante el analizador especificado. Es útil en escenarios de búsqueda de texto completo.

## Sintaxis de Analyze

```python
func.tokenize('The quick brown fox', 'english')
```

## Ejemplos de Analyze

```python
func.tokenize('The quick brown fox', 'english')

┌─────────────────────────┐
│ ["quick","brown","fox"] │
└─────────────────────────┘
```

## Sintaxis de SQL

```sql
TOKENIZE(<str>[, <analyzer>])
```

## Ejemplos de SQL

```sql
SELECT TOKENIZE('The quick brown fox', 'english');

┌─────────────────────────┐
│ ["quick","brown","fox"] │
└─────────────────────────┘
```
