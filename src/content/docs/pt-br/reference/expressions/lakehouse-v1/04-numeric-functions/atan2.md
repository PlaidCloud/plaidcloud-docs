---
title: ATAN2 (Lakehouse v1)
description: ATAN2 — retorna o arco tangente das duas variáveis x e y.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/atan2.md
---

Retorna o arco tangente das duas variáveis `x` e `y`. É semelhante a calcular o arco tangente de `y` / `x`, exceto que os sinais de ambos os argumentos são usados para determinar o quadrante do resultado. `ATAN(y, x)` é um sinônimo de `ATAN2(y, x)`.

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

## Exemplos de SQL

```sql
SELECT ATAN2(-2, 2);

┌─────────────────────┐
│   atan2((- 2), 2)   │
├─────────────────────┤
│ -0.7853981633974483 │
└─────────────────────┘
```
