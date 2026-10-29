---
title: STRRIGHT (Lakehouse v2)
description: STRRIGHT — devolve os N carateres mais à direita de uma cadeia. Alias de `RIGHT`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strright.md
---

Devolve os N carateres mais à direita de uma cadeia. Alias de `RIGHT`.

## Sintaxe do Analyze

```python
func.strright(<str>, <len>)
```

## Exemplos do Analyze

```python
func.strright('StarRocks', 5)

┌─────────┐
│ 'Rocks'  │
└─────────┘
```

## Sintaxe SQL

```sql
STRRIGHT(<str>, <len>)
```

## Exemplos SQL

```sql
SELECT STRRIGHT('StarRocks', 5);

┌───────┐
│ Rocks  │
└───────┘
```
