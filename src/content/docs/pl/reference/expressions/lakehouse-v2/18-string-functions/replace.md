---
title: REPLACE (Lakehouse v2)
description: REPLACE — zastępuje wszystkie wystąpienia podciągu innym podciągiem.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/replace.md
---

Zastępuje wszystkie wystąpienia podciągu innym podciągiem.

## Składnia Analyze

```python
func.replace(<str>, <old>, <new>)
```

## Przykłady Analyze

```python
func.replace('hello world', 'world', 'there')

┌───────────────┐
│ 'hello there'  │
└───────────────┘
```

## Składnia SQL

```sql
REPLACE(<str>, <old>, <new>)
```

## Przykłady SQL

```sql
SELECT REPLACE('hello world', 'world', 'there');

┌─────────────┐
│ hello there  │
└─────────────┘
```
