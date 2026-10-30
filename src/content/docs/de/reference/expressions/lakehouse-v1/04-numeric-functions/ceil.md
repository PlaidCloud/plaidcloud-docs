---
title: CEIL (Lakehouse v1)
description: CEIL – rundet die Zahl auf.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/ceil.md
---

Rundet die Zahl auf.

## Analyze-Syntax

```python
func.ceil( <x> )
```

## Analyze-Beispiele

```python
func.ceil((- 1.23))

┌─────────────────────┐
│ func.ceil((- 1.23)) │
├─────────────────────┤
│                  -1 │ 
└─────────────────────┘
```

## SQL-Syntax

```sql
CEIL( <x> )
```

## Aliase

- [CEILING](../ceiling)

## SQL-Beispiele

```sql
SELECT CEILING(-1.23), CEIL(-1.23);

┌────────────────────────────────────┐
│ ceiling((- 1.23)) │ ceil((- 1.23)) │
├───────────────────┼────────────────┤
│                -1 │             -1 │
└────────────────────────────────────┘
```
