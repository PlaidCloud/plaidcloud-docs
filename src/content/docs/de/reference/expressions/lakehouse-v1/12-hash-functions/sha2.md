---
title: SHA2 (Lakehouse v1)
description: SHA2 berechnet die Hash-Funktionen der SHA-2-Familie (SHA-224, SHA-256, SHA-384 und SHA-512).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/sha2.md
---

Berechnet die Hash-Funktionen der SHA-2-Familie (SHA-224, SHA-256, SHA-384 und SHA-512). Ist die Hash-Länge keiner der zulässigen Werte, ist der Rückgabewert NULL. Andernfalls ist das Ergebnis der Funktion ein Hash-Wert mit der gewünschten Anzahl von Bits als Zeichenfolge aus Hexadezimalziffern.

## Analyze-Syntax

```python
func.sha2(<expr>, <expr>)
```

## Analyze-Beispiele

```python
func.sha2('1234567890', 0)

┌──────────────────────────────────────────────────────────────────┐
│ func.sha2('1234567890', 0))                                      │
├──────────────────────────────────────────────────────────────────┤
│ c775e7b757ede630cd0aa1113bd102661ab38829ca52a6422ab782862f268646 │
└──────────────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
SHA2(<expr>, <expr>)
```

## SQL-Beispiele

```sql
SELECT SHA2('1234567890', 0);

┌──────────────────────────────────────────────────────────────────┐
│                       sha2('1234567890', 0)                      │
├──────────────────────────────────────────────────────────────────┤
│ c775e7b757ede630cd0aa1113bd102661ab38829ca52a6422ab782862f268646 │
└──────────────────────────────────────────────────────────────────┘
```
