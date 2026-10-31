---
title: "[ NOT ] BETWEEN (Lakehouse v1)"
description: "[ NOT ] BETWEEN — verdadeiro se um valor numérico, de texto ou de data estiver dentro (ou fora) do intervalo informado."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/between.md
---

Retorna `true` se o valor numérico ou de texto ` <expr>` estiver dentro dos limites inferior e superior definidos.

## Analyze Syntax

```python
table.column.between(<lower_limit>, <upper_limit>
```

## Analyze Examples

```python
table.column.between(0, 5)
```

## SQL Syntax

```sql
<expr> [ NOT ] BETWEEN <lower_limit> AND <upper_limit>
```

## SQL Examples

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
