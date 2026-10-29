---
title: CONV (Lakehouse v2)
description: CONV — converte um número de uma base para outra.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/conv.md
---

Converte um número de uma base para outra.

## Sintaxe do Analyze

```python
func.conv(<num>, <from_base>, <to_base>)
```

## Exemplos do Analyze

```python
func.conv('ff', 16, 10)

┌───────┐
│ '255'  │
└───────┘
```

## Sintaxe SQL

```sql
CONV(<num>, <from_base>, <to_base>)
```

## Exemplos de SQL

```sql
SELECT CONV('ff', 16, 10);

┌─────┐
│ 255  │
└─────┘
```
