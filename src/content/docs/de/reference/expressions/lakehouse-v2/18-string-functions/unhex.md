---
title: UNHEX (Lakehouse v2)
description: UNHEX — wandelt eine hexadezimale Zeichenfolge in eine Zeichenkette um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/unhex.md
---

Wandelt eine hexadezimale Zeichenfolge in eine Zeichenkette um.

## Analyze-Syntax

```python
func.unhex(<hex_str>)
```

## Analyze-Beispiele

```python
func.unhex('48656C6C6F')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## SQL-Syntax

```sql
UNHEX(<hex_str>)
```

## SQL-Beispiele

```sql
SELECT UNHEX('48656C6C6F');

┌───────┐
│ Hello  │
└───────┘
```
