---
title: TOMORROW (Lakehouse v1)
description: TOMORROW — devolve a data de amanhã, equivalente a today() + 1.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/tomorrow.md
---

Devolve a data de amanhã, equivalente a `today() + 1`.

## Sintaxe do Analyze

```python
func.tomorrow()
```

## Exemplos do Analyze

```python
func.tomorrow()
┌─────────────────┐
│ func.tomorrow() │
├─────────────────┤
│ 2021-09-03      │
└─────────────────┘
```

## Sintaxe SQL

```sql
TOMORROW()
```

## Tipo de Retorno

`DATE`, devolve a data no formato “YYYY-MM-DD”.

## Exemplos SQL

```sql
SELECT TOMORROW();
┌────────────┐
│ TOMORROW() │
├────────────┤
│ 2021-09-04 │
└────────────┘

SELECT TODAY()+1;
┌───────────────┐
│ (TODAY() + 1) │
├───────────────┤
│ 2021-09-04    │
└───────────────┘
```
