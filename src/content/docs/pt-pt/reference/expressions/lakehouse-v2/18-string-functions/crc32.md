---
title: CRC32 (Lakehouse v2)
description: CRC32 — devolve a soma de verificação CRC-32 de uma cadeia como inteiro sem sinal.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/crc32.md
---

Devolve a soma de verificação CRC-32 de uma cadeia como inteiro sem sinal.

## Sintaxe do Analyze

```python
func.crc32(<str>)
```

## Exemplos do Analyze

```python
func.crc32('hello')

┌───────────┐
│ 907060870  │
└───────────┘
```

## Sintaxe SQL

```sql
CRC32(<str>)
```

## Exemplos SQL

```sql
SELECT CRC32('hello');

┌───────────┐
│ 907060870  │
└───────────┘
```
