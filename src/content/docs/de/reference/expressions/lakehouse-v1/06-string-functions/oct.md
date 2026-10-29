---
title: OCT (Lakehouse v1)
description: OCT – gibt eine Zeichenfolgendarstellung des Oktalwerts von N zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/oct.md
---

Gibt eine Zeichenfolgendarstellung des Oktalwerts von N zurück.

## Analyze-Syntax

```python
func.oct(<expr>)
```

## Analyze-Beispiele

```python
func.oct(12)
┌─────────────────┐
│ func.oct(12)    │
├─────────────────┤
│ 014             │
└─────────────────┘
```

## SQL-Syntax

```sql
OCT(<expr>)
```

## SQL-Beispiele

```sql
SELECT OCT(12);
┌─────────┐
│ OCT(12) │
├─────────┤
│ 014     │
└─────────┘
```
