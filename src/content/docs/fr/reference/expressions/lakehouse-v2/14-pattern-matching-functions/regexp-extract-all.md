---
title: REGEXP_EXTRACT_ALL (Lakehouse v2)
description: REGEXP_EXTRACT_ALL — extrait toutes les sous-chaînes qui correspondent à un motif d'expression régulière.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-extract-all.md
---

Extrait toutes les sous-chaînes qui correspondent à un motif d'expression régulière.

## Syntaxe Analyze

```python
func.regexp_extract_all(<str>, <pattern>)
```

## Exemples Analyze

```python
func.regexp_extract_all('a1b2c3', '\\d+')

┌───────────────┐
│ ['1','2','3']  │
└───────────────┘
```

## Syntaxe SQL

```sql
REGEXP_EXTRACT_ALL(<str>, <pattern>)
```

## Exemples SQL

```sql
SELECT REGEXP_EXTRACT_ALL('a1b2c3', '\\d+');

┌───────────────┐
│ ["1","2","3"]  │
└───────────────┘
```
