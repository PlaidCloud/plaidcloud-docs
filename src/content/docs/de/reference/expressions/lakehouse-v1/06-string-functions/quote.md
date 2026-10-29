---
title: QUOTE (Lakehouse v1)
description: QUOTE – setzt eine Zeichenfolge in Anführungszeichen, sodass sie als korrekt maskierter Datenwert in einer SQL-Anweisung verwendet werden kann.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/quote.md
---

Setzt eine Zeichenfolge in Anführungszeichen, sodass das Ergebnis als korrekt maskierter Datenwert in einer SQL-Anweisung verwendet werden kann. 

## Analyze-Syntax

```python
func.quote(<str>)
```

## Analyze-Beispiele

```python
func.quote('Don\'t')
┌──────────────────────┐
│ func.quote('Don\'t') │
├──────────────────────┤
│  Don\'t!             │
└──────────────────────┘
```

## SQL-Syntax

```sql
QUOTE(<str>)
```

## SQL-Beispiele

```sql
SELECT QUOTE('Don\'t!');
┌─────────────────┐
│ QUOTE('Don't!') │
├─────────────────┤
│ Don\'t!         │
└─────────────────┘

SELECT QUOTE(NULL);
┌─────────────┐
│ QUOTE(NULL) │
├─────────────┤
│        NULL │
└─────────────┘
```
