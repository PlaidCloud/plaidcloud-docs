---
title: SHA2 (Lakehouse v1)
description: SHA2 — calcula a família de funções de hash SHA-2 (SHA-224, SHA-256, SHA-384 e SHA-512).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/sha2.md
---

Calcula a família de funções de hash SHA-2 (SHA-224, SHA-256, SHA-384 e SHA-512). Se o comprimento do hash não for um dos valores permitidos, o valor devolvido é NULL. Caso contrário, o resultado da função é um valor de hash com o número de bits pretendido, sob a forma de uma cadeia de dígitos hexadecimais.

## Sintaxe do Analyze

```python
func.sha2(<expr>, <expr>)
```

## Exemplos do Analyze

```python
func.sha2('1234567890', 0)

┌──────────────────────────────────────────────────────────────────┐
│ func.sha2('1234567890', 0))                                      │
├──────────────────────────────────────────────────────────────────┤
│ c775e7b757ede630cd0aa1113bd102661ab38829ca52a6422ab782862f268646 │
└──────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
SHA2(<expr>, <expr>)
```

## Exemplos de SQL

```sql
SELECT SHA2('1234567890', 0);

┌──────────────────────────────────────────────────────────────────┐
│                       sha2('1234567890', 0)                      │
├──────────────────────────────────────────────────────────────────┤
│ c775e7b757ede630cd0aa1113bd102661ab38829ca52a6422ab782862f268646 │
└──────────────────────────────────────────────────────────────────┘
```
