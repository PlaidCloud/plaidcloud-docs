---
title: NULL_OR_EMPTY (Lakehouse v2)
description: NULL_OR_EMPTY — verifica se uma cadeia é NULL ou está vazia. Devolve 1 se for verdadeiro, 0 caso contrário.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/null-or-empty.md
---

Verifica se uma cadeia é NULL ou está vazia. Devolve 1 se for verdadeiro, 0 caso contrário.

## Sintaxe do Analyze

```python
func.null_or_empty(<str>)
```

## Exemplos do Analyze

```python
func.null_or_empty('')

┌───┐
│ 1  │
└───┘
```

## Sintaxe SQL

```sql
NULL_OR_EMPTY(<str>)
```

## Exemplos SQL

```sql
SELECT NULL_OR_EMPTY('');

┌───┐
│ 1  │
└───┘
```
