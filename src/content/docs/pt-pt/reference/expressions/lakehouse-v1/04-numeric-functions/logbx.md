---
title: "LOG(b, x) (Lakehouse v1)"
description: LOG(b, x) — devolve o logaritmo de base b de x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/logbx.md
---

Devolve o logaritmo de base b de `x`. Se `x` for menor ou igual a 0.0E0, a função devolve NULL.

## Sintaxe do Analyze

```python
func.log( <b, x> )
```

## Exemplos do Analyze

```python
func.log(2, 65536)

┌────────────────────┐
│ func.log(2, 65536) │
├────────────────────┤
│                 16 │
└────────────────────┘
```

## Sintaxe SQL

```sql
LOG( <b, x> )
```

## Exemplos SQL

```sql
SELECT LOG(2, 65536);

┌───────────────┐
│ log(2, 65536) │
├───────────────┤
│            16 │
└───────────────┘
```
