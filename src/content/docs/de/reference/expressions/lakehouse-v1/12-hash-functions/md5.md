---
title: MD5 (Lakehouse v1)
description: MD5 berechnet eine 128-Bit-MD5-Prüfsumme für eine Zeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/md5.md
---

Berechnet eine 128-Bit-MD5-Prüfsumme für eine Zeichenfolge. Der Wert wird als Zeichenfolge aus 32 Hexadezimalziffern zurückgegeben oder als NULL, wenn das Argument NULL war.

## Analyze-Syntax

```python
func.md5(<expr>)
```

## Analyze-Beispiele

```python
func.md5('1234567890')

┌──────────────────────────────────────────┐
│ func.md5('1234567890')                   │
├──────────────────────────────────────────┤
│ e807f1fcf82d132f9bb018ca6738a19f         │
└──────────────────────────────────────────┘
```

## SQL-Syntax

```sql
MD5(<expr>)
```

## SQL-Beispiele

```sql
SELECT MD5('1234567890');

┌──────────────────────────────────┐
│         md5('1234567890')        │
├──────────────────────────────────┤
│ e807f1fcf82d132f9bb018ca6738a19f │
└──────────────────────────────────┘
```
