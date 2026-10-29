---
title: YESTERDAY (Lakehouse v1)
description: YESTERDAY — devolve a data de ontem, equivalente a today() - 1.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/yesterday.md
---

Devolve a data de ontem, equivalente a `today() - 1`.

## Sintaxe do Analyze

```python
func.yesterday()
```

## Exemplos do Analyze

```python
func.yesterday()
┌──────────────────┐
│ func.yesterday() │
├──────────────────┤
│ 2021-09-02       │
└──────────────────┘
```

## Sintaxe SQL

```sql
YESTERDAY()
```

## Tipo de Retorno

`DATE`, devolve a data no formato “YYYY-MM-DD”.

## Exemplos SQL

```sql
SELECT YESTERDAY();
┌─────────────┐
│ YESTERDAY() │
├─────────────┤
│ 2021-09-02  │
└─────────────┘

SELECT TODAY()-1;
┌───────────────┐
│ (TODAY() - 1) │
├───────────────┤
│ 2021-09-02    │
└───────────────┘
```
