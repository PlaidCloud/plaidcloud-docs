---
title: SHA (Lakehouse v1)
description: SHA — calcula uma soma de verificação SHA-1 de 160 bits para a string, conforme descrito na RFC 3174 (Secure Hash.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/sha.md
---

Calcula uma soma de verificação SHA-1 de 160 bits para a string, conforme descrito na RFC 3174 (Secure Hash Algorithm). O valor é retornado como uma string de 40 dígitos hexadecimais ou NULL se o argumento for NULL.

## Sintaxe no Analyze

```python
func.sha(<expr>)
```

## Exemplos no Analyze

```python
func.sha('1234567890')

┌──────────────────────────────────────────┐
│ func.sha('1234567890')                   │
├──────────────────────────────────────────┤
│ 01b307acba4f54f55aafc33bb06bbbf6ca803e9a │
└──────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
SHA(<expr>)
```

## Aliases

- [SHA1](../sha1)

## Exemplos de SQL

```sql
SELECT SHA('1234567890'), SHA1('1234567890');

┌─────────────────────────────────────────────────────────────────────────────────────┐
│             sha('1234567890')            │            sha1('1234567890')            │
├──────────────────────────────────────────┼──────────────────────────────────────────┤
│ 01b307acba4f54f55aafc33bb06bbbf6ca803e9a │ 01b307acba4f54f55aafc33bb06bbbf6ca803e9a │
└─────────────────────────────────────────────────────────────────────────────────────┘
```
