---
title: REGEXP_REPLACE (Lakehouse v2)
description: "Użyj funkcji dopasowywania wzorców REGEXP_REPLACE w PlaidCloud Lakehouse. Zastępuje podciągi pasujące do wzorca wyrażenia regularnego ciągiem zastępującym."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-replace.md
---

Zastępuje podciągi pasujące do wzorca wyrażenia regularnego ciągiem zastępującym.

## Składnia Analyze

```python
func.regexp_replace(<str>, <pattern>, <replacement>)
```

## Przykłady Analyze

```python
func.regexp_replace('hello   world', '\\s+', ' ')

┌───────────────┐
│ 'hello world'  │
└───────────────┘
```

## Składnia SQL

```sql
REGEXP_REPLACE(<str>, <pattern>, <replacement>)
```

## Przykłady SQL

```sql
SELECT REGEXP_REPLACE('hello   world', '\\s+', ' ');

┌─────────────┐
│ hello world  │
└─────────────┘
```
