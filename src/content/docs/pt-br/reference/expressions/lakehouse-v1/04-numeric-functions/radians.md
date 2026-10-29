---
title: RADIANS (Lakehouse v1)
description: RADIANS — retorna o argumento x convertido de graus para radianos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/radians.md
---

Retorna o argumento `x` convertido de graus para radianos.

## Sintaxe do Analyze

```python
func.radians( <x> )
```

## Exemplos do Analyze

```python
func.radians(90)

┌────────────────────┐
│  func.radians(90)  │
├────────────────────┤
│ 1.5707963267948966 │
└────────────────────┘
```

## Sintaxe SQL

```sql
RADIANS( <x> )
```

## Exemplos de SQL

```sql
SELECT RADIANS(90);

┌────────────────────┐
│     radians(90)    │
├────────────────────┤
│ 1.5707963267948966 │
└────────────────────┘
```
