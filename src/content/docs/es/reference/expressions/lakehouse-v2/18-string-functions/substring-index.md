---
title: SUBSTRING_INDEX (Lakehouse v2)
description: "Use la función de cadena SUBSTRING_INDEX en PlaidCloud Lakehouse. Devuelve una subcadena de una cadena antes o después de un número especificado de apariciones de un delimitador."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/substring-index.md
---

Devuelve una subcadena de una cadena antes o después de un número especificado de apariciones de un delimitador.

## Sintaxis de Analyze

```python
func.substring_index(<str>, <delim>, <count>)
```

## Ejemplos de Analyze

```python
func.substring_index('www.example.com', '.', 2)

┌───────────────┐
│ 'www.example'  │
└───────────────┘
```

## Sintaxis de SQL

```sql
SUBSTRING_INDEX(<str>, <delim>, <count>)
```

## Ejemplos de SQL

```sql
SELECT SUBSTRING_INDEX('www.example.com', '.', 2);

┌─────────────┐
│ www.example  │
└─────────────┘
```
