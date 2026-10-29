---
title: BLAKE3 (Lakehouse v1)
description: BLAKE3 berechnet eine 256-Bit-BLAKE3-Prüfsumme für eine Zeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/blake3.md
---

Berechnet eine 256-Bit-BLAKE3-Prüfsumme für eine Zeichenfolge. Der Wert wird als Zeichenfolge aus 64 Hexadezimalziffern zurückgegeben oder als NULL, wenn das Argument NULL war.

## Analyze-Syntax

```python
func.blake3(<expr>)
```

## Analyze-Beispiele

```python
func.blake3('1234567890')

┌──────────────────────────────────────────────────────────────────┐
│ func.blake3('1234567890')                                        │
├──────────────────────────────────────────────────────────────────┤
│ d12e417e04494572b561ba2c12c3d7f9e5107c4747e27b9a8a54f8480c63e841 │
└──────────────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
BLAKE3(<expr>)
```

## SQL-Beispiele

```sql
SELECT BLAKE3('1234567890');

┌──────────────────────────────────────────────────────────────────┐
│                       blake3('1234567890')                       │
├──────────────────────────────────────────────────────────────────┤
│ d12e417e04494572b561ba2c12c3d7f9e5107c4747e27b9a8a54f8480c63e841 │
└──────────────────────────────────────────────────────────────────┘
```
