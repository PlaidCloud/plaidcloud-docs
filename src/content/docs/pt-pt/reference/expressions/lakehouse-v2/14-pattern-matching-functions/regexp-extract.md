---
title: REGEXP_EXTRACT (Lakehouse v2)
description: REGEXP_EXTRACT — extrai a primeira subcadeia de caracteres que corresponde a um padrão de expressão regular.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-extract.md
---

Extrai a primeira subcadeia de caracteres que corresponde a um padrão de expressão regular.

## Sintaxe de Analyze

```python
func.regexp_extract(<str>, <pattern>[, <group>])
```

## Exemplos de Analyze

```python
func.regexp_extract('price: $42.50', '\\$(\\d+\\.\\d+)', 1)

┌─────────┐
│ '42.50'  │
└─────────┘
```

## Sintaxe SQL

```sql
REGEXP_EXTRACT(<str>, <pattern>[, <group>])
```

## Exemplos SQL

```sql
SELECT REGEXP_EXTRACT('price: $42.50', '\\$(\\d+\\.\\d+)', 1);

┌───────┐
│ 42.50  │
└───────┘
```
