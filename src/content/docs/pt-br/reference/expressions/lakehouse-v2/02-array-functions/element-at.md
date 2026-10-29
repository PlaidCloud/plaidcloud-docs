---
title: "ELEMENT_AT (Array, Lakehouse v2)"
description: ELEMENT_AT — retorna o elemento em uma posição especificada de um array (índice a partir de 1).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/element-at.md
---

Retorna o elemento em uma posição especificada de um array (índice a partir de 1).

## Sintaxe do Analyze

```python
func.element_at([10, 20, 30], 2)
```

## Exemplos do Analyze

```python
func.element_at([10, 20, 30], 2)

┌────┐
│ 20 │
└────┘
```

## Sintaxe SQL

```sql
ELEMENT_AT([10, 20, 30], 2)
```

## Exemplos SQL

```sql
SELECT ELEMENT_AT([10, 20, 30], 2);

┌────┐
│ 20 │
└────┘
```
