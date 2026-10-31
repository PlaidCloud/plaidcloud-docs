---
title: "LOG(b, x) (Lakehouse v1)"
description: LOG(b, x) — retorna o logaritmo de x na base b.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/logbx.md
---

Retorna o logaritmo de `x` na base b. Se `x` for menor ou igual a 0.0E0, a função retorna NULL.

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

## Exemplos de SQL

```sql
SELECT LOG(2, 65536);

┌───────────────┐
│ log(2, 65536) │
├───────────────┤
│            16 │
└───────────────┘
```
