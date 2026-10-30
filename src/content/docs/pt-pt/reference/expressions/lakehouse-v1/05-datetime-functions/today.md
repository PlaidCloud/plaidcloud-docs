---
title: TODAY (Lakehouse v1)
description: TODAY — devolve a data atual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/today.md
---

Devolve a data atual.

## Sintaxe do Analyze

```python
func.today()
```

## Exemplos do Analyze

```python
func.today()
┌──────────────┐
│ func.today() │
├──────────────┤
│ 2021-09-03   │
└──────────────┘
```

## Sintaxe SQL

```sql
TODAY()
```

## Tipo de Retorno

`DATE`, devolve a data no formato “YYYY-MM-DD”.

## Exemplos SQL

```sql
SELECT TODAY();
┌────────────┐
│ TODAY()    │
├────────────┤
│ 2021-09-03 │
└────────────┘
```
