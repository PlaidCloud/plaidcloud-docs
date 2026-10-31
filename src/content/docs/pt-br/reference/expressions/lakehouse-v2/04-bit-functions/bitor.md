---
title: BITOR (Lakehouse v2)
description: BITOR — retorna o OR bit a bit de dois valores numéricos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitor.md
---

Retorna o OR bit a bit de dois valores numéricos.

## Sintaxe do Analyze

```python
func.bitor(<x>, <y>)
```

## Exemplos do Analyze

```python
func.bitor(12, 10)

┌────┐
│ 14  │
└────┘
```

## Sintaxe SQL

```sql
BITOR(<x>, <y>)
```

## Exemplos SQL

```sql
SELECT BITOR(12, 10);

┌────┐
│ 14  │
└────┘
```
