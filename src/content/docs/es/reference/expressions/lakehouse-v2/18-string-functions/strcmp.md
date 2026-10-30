---
title: STRCMP (Lakehouse v2)
description: "Use la función de cadena STRCMP en PlaidCloud Lakehouse. Compara dos cadenas lexicográficamente. Devuelve 0 si son iguales, -1 si str1 < str2 y 1 si str1 > str2."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strcmp.md
---

Compara dos cadenas lexicográficamente. Devuelve 0 si son iguales, -1 si str1 &lt; str2 y 1 si str1 > str2.

## Sintaxis de Analyze

```python
func.strcmp(<str1>, <str2>)
```

## Ejemplos de Analyze

```python
func.strcmp('abc', 'abd')

┌────┐
│ -1  │
└────┘
```

## Sintaxis de SQL

```sql
STRCMP(<str1>, <str2>)
```

## Ejemplos de SQL

```sql
SELECT STRCMP('abc', 'abd');

┌────┐
│ -1  │
└────┘
```
