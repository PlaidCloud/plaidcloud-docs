---
title: MD5SUM (Lakehouse v2)
description: MD5SUM — devuelve el hash MD5 de varias cadenas concatenadas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/md5sum.md
---

Devuelve el hash MD5 de varias cadenas concatenadas.

## Sintaxis de Analyze

```python
func.md5sum(<str1>[, <str2>, ...])
```

## Ejemplos de Analyze

```python
func.md5sum('hello', 'world')

┌────────────────────────────────────┐
│ 'fc5e038d38a57032085441e7fe7010b0'  │
└────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
MD5SUM(<str1>[, <str2>, ...])
```

## Ejemplos de SQL

```sql
SELECT MD5SUM('hello', 'world');

┌──────────────────────────────────┐
│ fc5e038d38a57032085441e7fe7010b0  │
└──────────────────────────────────┘
```
