---
title: MD5 (Lakehouse v1)
description: MD5 calcula una suma de comprobación MD5 de 128 bits para una cadena.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/md5.md
---

Calcula una suma de comprobación MD5 de 128 bits para una cadena. El valor se devuelve como una cadena de 32 dígitos hexadecimales, o NULL si el argumento era NULL.

## Sintaxis de Analyze

```python
func.md5(<expr>)
```

## Ejemplos de Analyze

```python
func.md5('1234567890')

┌──────────────────────────────────────────┐
│ func.md5('1234567890')                   │
├──────────────────────────────────────────┤
│ e807f1fcf82d132f9bb018ca6738a19f         │
└──────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
MD5(<expr>)
```

## Ejemplos de SQL

```sql
SELECT MD5('1234567890');

┌──────────────────────────────────┐
│         md5('1234567890')        │
├──────────────────────────────────┤
│ e807f1fcf82d132f9bb018ca6738a19f │
└──────────────────────────────────┘
```
