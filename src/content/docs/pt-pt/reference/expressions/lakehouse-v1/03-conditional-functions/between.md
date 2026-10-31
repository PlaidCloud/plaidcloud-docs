---
title: "[ NOT ] BETWEEN (Lakehouse v1)"
description: "[ NOT ] BETWEEN — verdadeiro se um valor numérico, de cadeia de caracteres ou de data estiver dentro (ou fora) do intervalo indicado."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/between.md
---

Devolve `true` se a ` <expr>` numérica ou de cadeia de caracteres indicada se situar entre os limites inferior e superior definidos.

## Sintaxe do Analyze

```python
table.column.between(<lower_limit>, <upper_limit>
```

## Exemplos do Analyze

```python
table.column.between(0, 5)
```

## Sintaxe SQL

```sql
<expr> [ NOT ] BETWEEN <lower_limit> AND <upper_limit>
```

## Exemplos SQL

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
