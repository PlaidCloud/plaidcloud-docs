---
title: YESTERDAY (Lakehouse v1)
description: YESTERDAY – gibt das gestrige Datum zurück, entspricht today() - 1.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/yesterday.md
---

Gibt das gestrige Datum zurück, entspricht `today() - 1`.

## Analyze-Syntax

```python
func.yesterday()
```

## Analyze-Beispiele

```python
func.yesterday()
┌──────────────────┐
│ func.yesterday() │
├──────────────────┤
│ 2021-09-02       │
└──────────────────┘
```

## SQL-Syntax

```sql
YESTERDAY()
```

## Rückgabetyp

`DATE`, gibt das Datum im Format „YYYY-MM-DD“ zurück.

## SQL-Beispiele

```sql
SELECT YESTERDAY();
┌─────────────┐
│ YESTERDAY() │
├─────────────┤
│ 2021-09-02  │
└─────────────┘

SELECT TODAY()-1;
┌───────────────┐
│ (TODAY() - 1) │
├───────────────┤
│ 2021-09-02    │
└───────────────┘
```
