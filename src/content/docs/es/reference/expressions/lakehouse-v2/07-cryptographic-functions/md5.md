---
title: MD5 (Lakehouse v2)
description: MD5 — devuelve el hash MD5 de una cadena como una cadena hexadecimal de 32 caracteres.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/md5.md
---

Devuelve el hash MD5 de una cadena como una cadena hexadecimal de 32 caracteres.

## Sintaxis de Analyze

```python
func.md5(<str>)
```

## Ejemplos de Analyze

```python
func.md5('hello')

┌────────────────────────────────────┐
│ '5d41402abc4b2a76b9719d911017c592'  │
└────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
MD5(<str>)
```

## Ejemplos de SQL

```sql
SELECT MD5('hello');

┌──────────────────────────────────┐
│ 5d41402abc4b2a76b9719d911017c592  │
└──────────────────────────────────┘
```
