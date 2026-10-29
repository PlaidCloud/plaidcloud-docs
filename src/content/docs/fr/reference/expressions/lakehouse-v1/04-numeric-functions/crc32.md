---
title: CRC32 (Lakehouse v1)
description: CRC32 — renvoie la somme de contrôle CRC32 de x, où 'x' doit être une chaîne (et est traité comme telle si possible).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/crc32.md
---

Renvoie la somme de contrôle CRC32 de `x`, où 'x' doit être une chaîne ; s'il n'en est pas une, il est traité comme telle lorsque c'est possible.

## Syntaxe Analyze

```python
func.crc32( '<x>' )
```

## Exemples Analyze

```python
func.crc32('databend')

┌────────────────────────┐
│ func.crc32('databend') │
├────────────────────────┤
│             1177678456 │
└────────────────────────┘
```

## Syntaxe SQL

```sql
CRC32( '<x>' )
```

## Exemples SQL

```sql
SELECT CRC32('databend');

┌───────────────────┐
│ crc32('databend') │
├───────────────────┤
│        1177678456 │
└───────────────────┘
```
