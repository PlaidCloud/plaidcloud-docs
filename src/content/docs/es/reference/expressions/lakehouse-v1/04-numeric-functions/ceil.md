---
title: CEIL (Lakehouse v1)
description: CEIL — redondea el número hacia arriba.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/ceil.md
---

Redondea el número hacia arriba.

## Sintaxis de Analyze

```python
func.ceil( <x> )
```

## Ejemplos de Analyze

```python
func.ceil((- 1.23))

┌─────────────────────┐
│ func.ceil((- 1.23)) │
├─────────────────────┤
│                  -1 │ 
└─────────────────────┘
```

## Sintaxis de SQL

```sql
CEIL( <x> )
```

## Alias

- [CEILING](../ceiling)

## Ejemplos de SQL

```sql
SELECT CEILING(-1.23), CEIL(-1.23);

┌────────────────────────────────────┐
│ ceiling((- 1.23)) │ ceil((- 1.23)) │
├───────────────────┼────────────────┤
│                -1 │             -1 │
└────────────────────────────────────┘
```
