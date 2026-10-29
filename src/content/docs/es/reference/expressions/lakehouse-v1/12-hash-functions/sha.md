---
title: SHA (Lakehouse v1)
description: SHA calcula una suma de comprobación SHA-1 de 160 bits para la cadena, tal como se describe en la RFC 3174 (Secure Hash Algorithm).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/sha.md
---

Calcula una suma de comprobación SHA-1 de 160 bits para la cadena, tal como se describe en la RFC 3174 (Secure Hash Algorithm). El valor se devuelve como una cadena de 40 dígitos hexadecimales, o NULL si el argumento era NULL.

## Sintaxis de Analyze

```python
func.sha(<expr>)
```

## Ejemplos de Analyze

```python
func.sha('1234567890')

┌──────────────────────────────────────────┐
│ func.sha('1234567890')                   │
├──────────────────────────────────────────┤
│ 01b307acba4f54f55aafc33bb06bbbf6ca803e9a │
└──────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
SHA(<expr>)
```

## Alias

- [SHA1](../sha1)

## Ejemplos de SQL

```sql
SELECT SHA('1234567890'), SHA1('1234567890');

┌─────────────────────────────────────────────────────────────────────────────────────┐
│             sha('1234567890')            │            sha1('1234567890')            │
├──────────────────────────────────────────┼──────────────────────────────────────────┤
│ 01b307acba4f54f55aafc33bb06bbbf6ca803e9a │ 01b307acba4f54f55aafc33bb06bbbf6ca803e9a │
└─────────────────────────────────────────────────────────────────────────────────────┘
```
