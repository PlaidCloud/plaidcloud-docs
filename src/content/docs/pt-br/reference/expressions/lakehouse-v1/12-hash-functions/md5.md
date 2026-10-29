---
title: MD5 (Lakehouse v1)
description: MD5 — calcula uma soma de verificação MD5 de 128 bits para uma string.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/md5.md
---

Calcula uma soma de verificação MD5 de 128 bits para uma string. O valor é retornado como uma string de 32 dígitos hexadecimais ou NULL se o argumento for NULL.

## Sintaxe no Analyze

```python
func.md5(<expr>)
```

## Exemplos no Analyze

```python
func.md5('1234567890')

┌──────────────────────────────────────────┐
│ func.md5('1234567890')                   │
├──────────────────────────────────────────┤
│ e807f1fcf82d132f9bb018ca6738a19f         │
└──────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
MD5(<expr>)
```

## Exemplos de SQL

```sql
SELECT MD5('1234567890');

┌──────────────────────────────────┐
│         md5('1234567890')        │
├──────────────────────────────────┤
│ e807f1fcf82d132f9bb018ca6738a19f │
└──────────────────────────────────┘
```
