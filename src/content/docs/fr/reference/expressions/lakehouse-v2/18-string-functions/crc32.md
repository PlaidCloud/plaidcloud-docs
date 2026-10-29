---
title: CRC32 (Lakehouse v2)
description: CRC32 — renvoie la somme de contrôle CRC-32 d'une chaîne sous la forme d'un entier non signé.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/crc32.md
---

Renvoie la somme de contrôle CRC-32 d'une chaîne sous la forme d'un entier non signé.

## Syntaxe Analyze

```python
func.crc32(<str>)
```

## Exemples Analyze

```python
func.crc32('hello')

┌───────────┐
│ 907060870  │
└───────────┘
```

## Syntaxe SQL

```sql
CRC32(<str>)
```

## Exemples SQL

```sql
SELECT CRC32('hello');

┌───────────┐
│ 907060870  │
└───────────┘
```
