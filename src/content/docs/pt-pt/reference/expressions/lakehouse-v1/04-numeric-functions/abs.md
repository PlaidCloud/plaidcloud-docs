---
title: ABS (Lakehouse v1)
description: ABS — devolve o valor absoluto de x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/abs.md
---

Devolve o valor absoluto de `x`.

## Sintaxe do Analyze

```python
func.abs( <x> )
```

## Exemplos do Analyze

```python
func.abs((- 5))

┌─────────────────┐
│ func.abs((- 5)) │
├─────────────────┤
│               5 │
└─────────────────┘
```

## Sintaxe SQL

```sql
ABS( <x> )
```

## Exemplos SQL

```sql
SELECT ABS(-5);

┌────────────┐
│ abs((- 5)) │
├────────────┤
│          5 │
└────────────┘
```
