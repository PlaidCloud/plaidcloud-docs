---
title: "[ NOT ] BETWEEN (Lakehouse v1)"
description: "[ NOT ] BETWEEN — verdadero si un valor numérico, de cadena o de fecha se encuentra dentro (o fuera) del intervalo indicado."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/between.md
---

Devuelve `true` si la ` <expr>` numérica o de cadena indicada se encuentra dentro de los límites inferior y superior definidos.

## Sintaxis de Analyze

```python
table.column.between(<lower_limit>, <upper_limit>
```

## Ejemplos de Analyze

```python
table.column.between(0, 5)
```

## Sintaxis de SQL

```sql
<expr> [ NOT ] BETWEEN <lower_limit> AND <upper_limit>
```

## Ejemplos de SQL

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
