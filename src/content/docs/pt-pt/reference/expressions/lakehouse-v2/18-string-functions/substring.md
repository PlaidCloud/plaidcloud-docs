---
title: SUBSTRING (Lakehouse v2)
description: SUBSTRING — devolve uma subcadeia a partir de uma posição especificada. Alias de `SUBSTR`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/substring.md
---

Devolve uma subcadeia a partir de uma posição especificada. Alias de `SUBSTR`.

## Sintaxe do Analyze

```python
func.substring(<str>, <pos>[, <len>])
```

## Exemplos do Analyze

```python
func.substring('StarRocks', 1, 4)

┌────────┐
│ 'Star'  │
└────────┘
```

## Sintaxe SQL

```sql
SUBSTRING(<str>, <pos>[, <len>])
```

## Exemplos SQL

```sql
SELECT SUBSTRING('StarRocks', 1, 4);

┌──────┐
│ Star  │
└──────┘
```
