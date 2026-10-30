---
title: ASCII (Lakehouse v2)
description: ASCII — Gibt den ASCII-Code des ersten Zeichens einer Zeichenfolge zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ascii.md
---

Gibt den ASCII-Code des ersten Zeichens einer Zeichenfolge zurück.

## Analyze-Syntax

```python
func.ascii(<str>)
```

## Analyze-Beispiele

```python
func.ascii('A')

┌────┐
│ 65  │
└────┘
```

## SQL-Syntax

```sql
ASCII(<str>)
```

## SQL-Beispiele

```sql
SELECT ASCII('A');

┌────┐
│ 65  │
└────┘
```
