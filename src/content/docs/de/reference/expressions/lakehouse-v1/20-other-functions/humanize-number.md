---
title: HUMANIZE_NUMBER (Lakehouse v1)
description: HUMANIZE_NUMBER gibt eine lesbare Zahl zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/humanize-number.md
---

Gibt eine lesbare Zahl zurück.

## Analyze-Syntax

```python
func.humanize_number(x);
```

## Analyze-Beispiele

```python
func.humanize_number(1000 * 1000)
┌─────────────────────────────────────┐
│ func.humanize_number((1000 * 1000)) │
├─────────────────────────────────────┤
│ 1 million                           │
└─────────────────────────────────────┘
```

## SQL-Syntax

```sql
HUMANIZE_NUMBER(x);
```

## Argumente

| Argumente | Beschreibung               |
|-----------|----------------------------|
| x         | Der numerische Wert.       |


## Rückgabetyp

Zeichenfolge.

## SQL-Beispiele

```sql
SELECT HUMANIZE_NUMBER(1000 * 1000)
┌─────────────────────────┐
│ HUMANIZE_NUMBER((1000 * 1000)) │
├─────────────────────────┤
│ 1 million               │
└─────────────────────────┘
```
