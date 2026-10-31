---
title: MD5 (Lakehouse v2)
description: MD5 – gibt den MD5-Hash einer Zeichenfolge als hexadezimale Zeichenfolge mit 32 Zeichen zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/md5.md
---

Gibt den MD5-Hash einer Zeichenfolge als hexadezimale Zeichenfolge mit 32 Zeichen zurück.

## Analyze-Syntax

```python
func.md5(<str>)
```

## Analyze-Beispiele

```python
func.md5('hello')

┌────────────────────────────────────┐
│ '5d41402abc4b2a76b9719d911017c592'  │
└────────────────────────────────────┘
```

## SQL-Syntax

```sql
MD5(<str>)
```

## SQL-Beispiele

```sql
SELECT MD5('hello');

┌──────────────────────────────────┐
│ 5d41402abc4b2a76b9719d911017c592  │
└──────────────────────────────────┘
```
