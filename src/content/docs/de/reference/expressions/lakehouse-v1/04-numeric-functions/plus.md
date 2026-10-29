---
title: PLUS (Lakehouse v1)
description: PLUS – berechnet die Summe zweier numerischer oder Dezimalwerte.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/plus.md
---

Berechnet die Summe zweier numerischer oder Dezimalwerte.

## Analyze-Syntax

```python
func.plus(<number1>, <number2>)
```

## Analyze-Beispiele

```python
func.plus(1, 2.3)

┌────────────────────┐
│  func.plus(1, 2.3) │
├────────────────────┤
│ 3.3                │
└────────────────────┘
```

## SQL-Syntax

```sql
PLUS(<number1>, <number2>)
```

## Aliase

- [ADD](../add)

## SQL-Beispiele

```sql
SELECT ADD(1, 2.3), PLUS(1, 2.3);

┌───────────────────────────────┐
│  add(1, 2.3)  │  plus(1, 2.3) │
├───────────────┼───────────────┤
│ 3.3           │ 3.3           │
└───────────────────────────────┘
```
