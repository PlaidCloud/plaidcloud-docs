---
title: TRUNCATE (Lakehouse v1)
description: TRUNCATE – gibt die Zahl x zurück, auf d Dezimalstellen abgeschnitten.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/truncate.md
---

Gibt die Zahl `x` zurück, auf `d` Dezimalstellen abgeschnitten. Ist `d` gleich 0, hat das Ergebnis weder Dezimalpunkt noch Nachkommastellen. `d` kann negativ sein, sodass `d` Stellen links vom Dezimalpunkt des Werts `x` zu null werden. Der maximale Absolutwert für `d` ist 30; darüber hinausgehende Stellen (über 30 bzw. -30) werden abgeschnitten.

## Analyze-Syntax

```python
func.truncate( <x, d> )
```

## Analyze-Beispiele

```python
func.truncate(1.223, 1)

┌─────────────────────────┐
│ func.truncate(1.223, 1) │
├─────────────────────────┤
│                     1.2 │
└─────────────────────────┘
```

## SQL-Syntax

```sql
TRUNCATE( <x, d> )
```

## SQL-Beispiele

```sql
SELECT TRUNCATE(1.223, 1);

┌────────────────────┐
│ truncate(1.223, 1) │
├────────────────────┤
│ 1.2                │
└────────────────────┘
```
