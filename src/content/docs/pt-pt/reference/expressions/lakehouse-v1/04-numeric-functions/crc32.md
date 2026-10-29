---
title: CRC32 (Lakehouse v1)
description: CRC32 — devolve a soma de verificação CRC32 de x, em que se espera que 'x' seja uma cadeia de caracteres e, se possível, é tratado como tal.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/crc32.md
---

Devolve a soma de verificação CRC32 de `x`, em que se espera que 'x' seja uma cadeia de caracteres e, se possível, é tratado como tal caso não o seja.

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

## Exemplos SQL

```sql
SELECT CRC32('databend');

┌───────────────────┐
│ crc32('databend') │
├───────────────────┤
│        1177678456 │
└───────────────────┘
```
