---
title: MD5SUM (Lakehouse v2)
description: MD5SUM – gibt den MD5-Hash mehrerer aneinandergehängter Zeichenfolgen zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/md5sum.md
---

Gibt den MD5-Hash mehrerer aneinandergehängter Zeichenfolgen zurück.

## Analyze-Syntax

```python
func.md5sum(<str1>[, <str2>, ...])
```

## Analyze-Beispiele

```python
func.md5sum('hello', 'world')

┌────────────────────────────────────┐
│ 'fc5e038d38a57032085441e7fe7010b0'  │
└────────────────────────────────────┘
```

## SQL-Syntax

```sql
MD5SUM(<str1>[, <str2>, ...])
```

## SQL-Beispiele

```sql
SELECT MD5SUM('hello', 'world');

┌──────────────────────────────────┐
│ fc5e038d38a57032085441e7fe7010b0  │
└──────────────────────────────────┘
```
