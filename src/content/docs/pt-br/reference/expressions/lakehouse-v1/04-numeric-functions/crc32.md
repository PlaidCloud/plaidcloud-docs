---
title: CRC32 (Lakehouse v1)
description: CRC32 — retorna a soma de verificação CRC32 de x, em que 'x' deve ser uma string e, se possível, é tratado como tal.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/crc32.md
---

Retorna a soma de verificação CRC32 de `x`, em que 'x' deve ser uma string e, se possível, é tratado como tal caso não seja.

## Sintaxe do Analyze

```python
func.crc32( '<x>' )
```

## Exemplos do Analyze

```python
func.crc32('databend')

┌────────────────────────┐
│ func.crc32('databend') │
├────────────────────────┤
│             1177678456 │
└────────────────────────┘
```

## Sintaxe SQL

```sql
CRC32( '<x>' )
```

## Exemplos de SQL

```sql
SELECT CRC32('databend');

┌───────────────────┐
│ crc32('databend') │
├───────────────────┤
│        1177678456 │
└───────────────────┘
```
