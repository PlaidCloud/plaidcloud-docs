---
title: CEIL (Lakehouse v1)
description: CEIL — zaokrągla liczbę w górę.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/ceil.md
---

Zaokrągla liczbę w górę.

## Składnia Analyze

```python
func.ceil( <x> )
```

## Przykłady Analyze

```python
func.ceil((- 1.23))

┌─────────────────────┐
│ func.ceil((- 1.23)) │
├─────────────────────┤
│                  -1 │ 
└─────────────────────┘
```

## Składnia SQL

```sql
CEIL( <x> )
```

## Aliasy

- [CEILING](../ceiling)

## Przykłady SQL

```sql
SELECT CEILING(-1.23), CEIL(-1.23);

┌────────────────────────────────────┐
│ ceiling((- 1.23)) │ ceil((- 1.23)) │
├───────────────────┼────────────────┤
│                -1 │             -1 │
└────────────────────────────────────┘
```
