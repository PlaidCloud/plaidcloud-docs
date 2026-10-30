---
title: "[ NOT ] BETWEEN (Lakehouse v1)"
description: "[ NOT ] BETWEEN – wahr, wenn ein numerischer Wert, eine Zeichenfolge oder ein Datumswert innerhalb (oder außerhalb) des angegebenen Bereichs liegt."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/between.md
---

Gibt `true` zurück, wenn der angegebene numerische oder Zeichenfolgen-` <expr>` innerhalb der festgelegten Unter- und Obergrenze liegt.

## Analyze-Syntax

```python
table.column.between(<lower_limit>, <upper_limit>
```

## Analyze-Beispiele

```python
table.column.between(0, 5)
```

## SQL-Syntax

```sql
<expr> [ NOT ] BETWEEN <lower_limit> AND <upper_limit>
```

## SQL-Beispiele

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
