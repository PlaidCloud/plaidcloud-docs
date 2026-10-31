---
title: HEX (Lakehouse v2)
description: HEX — renvoie la représentation hexadécimale d'une chaîne ou d'un nombre.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/hex.md
---

Renvoie la représentation hexadécimale d'une chaîne ou d'un nombre.

## Syntaxe Analyze

```python
func.hex(<expr>)
```

## Exemples Analyze

```python
func.hex(255)

┌──────┐
│ 'FF'  │
└──────┘
```

## Syntaxe SQL

```sql
HEX(<expr>)
```

## Exemples SQL

```sql
SELECT HEX(255);

┌────┐
│ FF  │
└────┘
```
