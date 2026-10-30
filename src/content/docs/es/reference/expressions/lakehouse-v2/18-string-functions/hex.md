---
title: HEX (Lakehouse v2)
description: HEX — Devuelve la representación hexadecimal de una cadena o un número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/hex.md
---

Devuelve la representación hexadecimal de una cadena o un número.

## Sintaxis de Analyze

```python
func.hex(<expr>)
```

## Ejemplos de Analyze

```python
func.hex(255)

┌──────┐
│ 'FF'  │
└──────┘
```

## Sintaxis de SQL

```sql
HEX(<expr>)
```

## Ejemplos de SQL

```sql
SELECT HEX(255);

┌────┐
│ FF  │
└────┘
```
