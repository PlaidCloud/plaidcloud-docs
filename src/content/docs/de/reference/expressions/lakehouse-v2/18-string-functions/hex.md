---
title: HEX (Lakehouse v2)
description: HEX — Gibt die hexadezimale Darstellung einer Zeichenfolge oder Zahl zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/hex.md
---

Gibt die hexadezimale Darstellung einer Zeichenfolge oder Zahl zurück.

## Analyze-Syntax

```python
func.hex(<expr>)
```

## Analyze-Beispiele

```python
func.hex(255)

┌──────┐
│ 'FF'  │
└──────┘
```

## SQL-Syntax

```sql
HEX(<expr>)
```

## SQL-Beispiele

```sql
SELECT HEX(255);

┌────┐
│ FF  │
└────┘
```
