---
title: CEIL (Lakehouse v1)
description: CEIL — arrondit le nombre à l'entier supérieur.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/ceil.md
---

Arrondit le nombre à l'entier supérieur.

## Syntaxe Analyze

```python
func.ceil( <x> )
```

## Exemples Analyze

```python
func.ceil((- 1.23))

┌─────────────────────┐
│ func.ceil((- 1.23)) │
├─────────────────────┤
│                  -1 │ 
└─────────────────────┘
```

## Syntaxe SQL

```sql
CEIL( <x> )
```

## Alias

- [CEILING](../ceiling)

## Exemples SQL

```sql
SELECT CEILING(-1.23), CEIL(-1.23);

┌────────────────────────────────────┐
│ ceiling((- 1.23)) │ ceil((- 1.23)) │
├───────────────────┼────────────────┤
│                -1 │             -1 │
└────────────────────────────────────┘
```
