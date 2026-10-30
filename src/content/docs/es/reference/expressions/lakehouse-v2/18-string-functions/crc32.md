---
title: CRC32 (Lakehouse v2)
description: CRC32 — Devuelve la suma de comprobación CRC-32 de una cadena como un entero sin signo.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/crc32.md
---

Devuelve la suma de comprobación CRC-32 de una cadena como un entero sin signo.

## Sintaxis de Analyze

```python
func.crc32(<str>)
```

## Ejemplos de Analyze

```python
func.crc32('hello')

┌───────────┐
│ 907060870  │
└───────────┘
```

## Sintaxis de SQL

```sql
CRC32(<str>)
```

## Ejemplos de SQL

```sql
SELECT CRC32('hello');

┌───────────┐
│ 907060870  │
└───────────┘
```
