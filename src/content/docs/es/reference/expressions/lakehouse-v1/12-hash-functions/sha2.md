---
title: SHA2 (Lakehouse v1)
description: SHA2 calcula la familia de funciones hash SHA-2 (SHA-224, SHA-256, SHA-384 y SHA-512).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/sha2.md
---

Calcula la familia de funciones hash SHA-2 (SHA-224, SHA-256, SHA-384 y SHA-512). Si la longitud del hash no es uno de los valores permitidos, el valor devuelto es NULL. De lo contrario, el resultado de la función es un valor hash con el número de bits deseado, expresado como una cadena de dígitos hexadecimales.

## Sintaxis de Analyze

```python
func.sha2(<expr>, <expr>)
```

## Ejemplos de Analyze

```python
func.sha2('1234567890', 0)

┌──────────────────────────────────────────────────────────────────┐
│ func.sha2('1234567890', 0))                                      │
├──────────────────────────────────────────────────────────────────┤
│ c775e7b757ede630cd0aa1113bd102661ab38829ca52a6422ab782862f268646 │
└──────────────────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
SHA2(<expr>, <expr>)
```

## Ejemplos de SQL

```sql
SELECT SHA2('1234567890', 0);

┌──────────────────────────────────────────────────────────────────┐
│                       sha2('1234567890', 0)                      │
├──────────────────────────────────────────────────────────────────┤
│ c775e7b757ede630cd0aa1113bd102661ab38829ca52a6422ab782862f268646 │
└──────────────────────────────────────────────────────────────────┘
```
