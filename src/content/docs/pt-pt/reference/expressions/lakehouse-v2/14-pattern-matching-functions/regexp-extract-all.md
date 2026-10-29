---
title: REGEXP_EXTRACT_ALL (Lakehouse v2)
description: REGEXP_EXTRACT_ALL — extrai todas as subcadeias de caracteres que correspondem a um padrão de expressão regular.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-extract-all.md
---

Extrai todas as subcadeias de caracteres que correspondem a um padrão de expressão regular.

## Sintaxe de Analyze

```python
func.regexp_extract_all(<str>, <pattern>)
```

## Exemplos de Analyze

```python
func.regexp_extract_all('a1b2c3', '\\d+')

┌───────────────┐
│ ['1','2','3']  │
└───────────────┘
```

## Sintaxe SQL

```sql
REGEXP_EXTRACT_ALL(<str>, <pattern>)
```

## Exemplos SQL

```sql
SELECT REGEXP_EXTRACT_ALL('a1b2c3', '\\d+');

┌───────────────┐
│ ["1","2","3"]  │
└───────────────┘
```
