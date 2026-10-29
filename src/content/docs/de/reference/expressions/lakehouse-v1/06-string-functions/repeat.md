---
title: REPEAT (Lakehouse v1)
description: REPEAT – gibt eine Zeichenfolge zurück, die aus der count-fach wiederholten Zeichenfolge str besteht.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/repeat.md
---

Gibt eine Zeichenfolge zurück, die aus der count-fach wiederholten Zeichenfolge str besteht. Ist count kleiner als 1, wird eine leere Zeichenfolge zurückgegeben. Gibt NULL zurück, wenn str oder count NULL ist.

## Analyze-Syntax

```python
func.repeat(<str>, <count>)
```

## Analyze-Beispiele

```python
func.repeat(<str>, <count>)
┌─────────────────────────┐
│ func.repeat('plaid', 3) │
├─────────────────────────┤
│ plaidplaidplaid         │
└─────────────────────────┘
```

## SQL-Syntax

```sql
REPEAT(<str>, <count>)
```

## Argumente

| Argumente | Beschreibung      |
|-----------|-------------------|
| `<str>`   | Die Zeichenfolge. |
| `<count>` | Die Zahl.         |

## SQL-Beispiele

```sql
SELECT REPEAT('databend', 3);
┌──────────────────────────┐
│ REPEAT('databend', 3)    │
├──────────────────────────┤
│ databenddatabenddatabend │
└──────────────────────────┘

SELECT REPEAT('databend', 0);
┌───────────────────────┐
│ REPEAT('databend', 0) │
├───────────────────────┤
│                       │
└───────────────────────┘

SELECT REPEAT('databend', NULL);
┌──────────────────────────┐
│ REPEAT('databend', NULL) │
├──────────────────────────┤
│                     NULL │
└──────────────────────────┘
```
