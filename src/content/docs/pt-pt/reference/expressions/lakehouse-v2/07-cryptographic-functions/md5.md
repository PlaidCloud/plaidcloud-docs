---
title: MD5 (Lakehouse v2)
description: MD5 — devolve o hash MD5 de uma cadeia como uma cadeia hexadecimal de 32 carateres.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/md5.md
---

Devolve o hash MD5 de uma cadeia como uma cadeia hexadecimal de 32 carateres.

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
