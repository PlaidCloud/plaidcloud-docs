---
title: CRC32 (Lakehouse v1)
description: CRC32 — devuelve la suma de comprobación CRC32 de x, donde se espera que 'x' sea una cadena y, si es posible, se trata como tal.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/crc32.md
---

Devuelve la suma de comprobación CRC32 de `x`, donde se espera que 'x' sea una cadena y, si no lo es, se trata como tal siempre que sea posible.

## Sintaxis de Analyze

```python
func.crc32( '<x>' )
```

## Ejemplos de Analyze

```python
func.crc32('databend')

┌────────────────────────┐
│ func.crc32('databend') │
├────────────────────────┤
│             1177678456 │
└────────────────────────┘
```

## Sintaxis de SQL

```sql
CRC32( '<x>' )
```

## Ejemplos de SQL

```sql
SELECT CRC32('databend');

┌───────────────────┐
│ crc32('databend') │
├───────────────────┤
│        1177678456 │
└───────────────────┘
```
