---
title: "[ NOT ] IN (Lakehouse v1)"
description: "[ NOT ] IN — verdadeiro se um valor for igual (ou diferente) a qualquer item de uma lista explícita."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/in.md
---

Verifica se um valor está (ou não está) em uma lista explícita.

## Sintaxe do Analyze

```python
table.columns.in_((<value1>, <value2> ...))
```

## Exemplos do Analyze

```python
table.columns.in_((<value1>, <value2> ...))

┌──────────────────────────┐
│ table.column.in_((2, 3)) │
├──────────────────────────┤
│ true                     │
└──────────────────────────┘
```

## Sintaxe SQL

```sql
<value> [ NOT ] IN (<value1>, <value2> ...)
```

## Exemplos de SQL

```sql
SELECT 1 NOT IN (2, 3);

┌────────────────┐
│ 1 not in(2, 3) │
├────────────────┤
│ true           │
└────────────────┘
```
