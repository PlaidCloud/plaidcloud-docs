---
title: REGEXP_EXTRACT_ALL (Lakehouse v2)
description: REGEXP_EXTRACT_ALL — wyodrębnia wszystkie podciągi pasujące do wzorca wyrażenia regularnego.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-extract-all.md
---

Wyodrębnia wszystkie podciągi pasujące do wzorca wyrażenia regularnego.

## Składnia Analyze

```python
func.regexp_extract_all(<str>, <pattern>)
```

## Przykłady Analyze

```python
func.regexp_extract_all('a1b2c3', '\\d+')

┌───────────────┐
│ ['1','2','3']  │
└───────────────┘
```

## Składnia SQL

```sql
REGEXP_EXTRACT_ALL(<str>, <pattern>)
```

## Przykłady SQL

```sql
SELECT REGEXP_EXTRACT_ALL('a1b2c3', '\\d+');

┌───────────────┐
│ ["1","2","3"]  │
└───────────────┘
```
