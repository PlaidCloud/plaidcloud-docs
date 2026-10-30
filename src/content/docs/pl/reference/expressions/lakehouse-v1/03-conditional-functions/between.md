---
title: "[ NOT ] BETWEEN (Lakehouse v1)"
description: "[ NOT ] BETWEEN — zwraca true, jeśli wartość liczbowa, tekstowa lub data leży wewnątrz (albo poza) podanym zakresem."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/between.md
---

Zwraca `true`, jeśli podane wyrażenie liczbowe lub tekstowe ` <expr>` mieści się między zdefiniowanym dolnym i górnym limitem.

## Składnia Analyze

```python
table.column.between(<lower_limit>, <upper_limit>
```

## Przykłady Analyze

```python
table.column.between(0, 5)
```

## Składnia SQL

```sql
<expr> [ NOT ] BETWEEN <lower_limit> AND <upper_limit>
```

## Przykłady SQL

```sql
SELECT 'true' WHERE 5 BETWEEN 0 AND 5;

┌────────┐
│ 'true' │
├────────┤
│ true   │
└────────┘

SELECT 'true' WHERE 'data' BETWEEN 'data' AND 'databendcloud';

┌────────┐
│ 'true' │
├────────┤
│ true   │
└────────┘
```
