---
title: CEIL (Lakehouse v1)
description: CEIL — arredonda o número por excesso.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/ceil.md
---

Arredonda o número por excesso.

## Sintaxe do Analyze

```python
func.ceil( <x> )
```

## Exemplos do Analyze

```python
func.ceil((- 1.23))

┌─────────────────────┐
│ func.ceil((- 1.23)) │
├─────────────────────┤
│                  -1 │ 
└─────────────────────┘
```

## Sintaxe SQL

```sql
CEIL( <x> )
```

## Aliases

- [CEILING](../ceiling)

## Exemplos SQL

```sql
SELECT CEILING(-1.23), CEIL(-1.23);

┌────────────────────────────────────┐
│ ceiling((- 1.23)) │ ceil((- 1.23)) │
├───────────────────┼────────────────┤
│                -1 │             -1 │
└────────────────────────────────────┘
```
