---
title: MD5 (Lakehouse v2)
description: MD5 — retorna o hash MD5 de uma string como uma string hexadecimal de 32 caracteres.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/md5.md
---

Retorna o hash MD5 de uma string como uma string hexadecimal de 32 caracteres.

## Sintaxe do Analyze

```python
func.md5(<str>)
```

## Exemplos do Analyze

```python
func.md5('hello')

┌────────────────────────────────────┐
│ '5d41402abc4b2a76b9719d911017c592'  │
└────────────────────────────────────┘
```

## Sintaxe SQL

```sql
MD5(<str>)
```

## Exemplos SQL

```sql
SELECT MD5('hello');

┌──────────────────────────────────┐
│ 5d41402abc4b2a76b9719d911017c592  │
└──────────────────────────────────┘
```
