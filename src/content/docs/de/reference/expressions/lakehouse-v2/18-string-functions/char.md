---
title: CHAR (Lakehouse v2)
description: CHAR — gibt das Zeichen für einen angegebenen ASCII-Code zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/char.md
---

Gibt das Zeichen für einen angegebenen ASCII-Code zurück.

## Analyze-Syntax

```python
func.char(<code>)
```

## Analyze-Beispiele

```python
func.char(65)

┌─────┐
│ 'A'  │
└─────┘
```

## SQL-Syntax

```sql
CHAR(<code>)
```

## SQL-Beispiele

```sql
SELECT CHAR(65);

┌───┐
│ A  │
└───┘
```
