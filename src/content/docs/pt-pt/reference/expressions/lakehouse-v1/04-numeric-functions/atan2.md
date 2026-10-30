---
title: ATAN2 (Lakehouse v1)
description: ATAN2 — devolve o arco tangente das duas variáveis x e y.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/atan2.md
---

Devolve o arco tangente das duas variáveis `x` e `y`. É semelhante ao cálculo do arco tangente de `y` / `x`, exceto que os sinais de ambos os argumentos são usados para determinar o quadrante do resultado. `ATAN(y, x)` é sinónimo de `ATAN2(y, x)`.

## Sintaxe do Analyze

```python
func.atan2( <y, x> )
```

## Exemplos do Analyze

```python
func.atan2((- 2), 2)

┌─────────────────────┐
│ func.atan2((- 2), 2)│
├─────────────────────┤
│ -0.7853981633974483 │
└─────────────────────┘
```

## Sintaxe SQL

```sql
ATAN2( <y, x> )
```

## Exemplos SQL

```sql
SELECT ATAN2(-2, 2);

┌─────────────────────┐
│   atan2((- 2), 2)   │
├─────────────────────┤
│ -0.7853981633974483 │
└─────────────────────┘
```
