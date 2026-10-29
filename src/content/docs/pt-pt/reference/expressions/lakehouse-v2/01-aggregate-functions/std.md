---
title: STD (Lakehouse v2)
description: STD — devolve o desvio-padrão populacional. Alias de `STDDEV_POP`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/std.md
---

Devolve o desvio-padrão populacional. Alias de `STDDEV_POP`.

## Sintaxe do Analyze

```python
func.std(get_column(table, 'score'))
```

## Exemplos do Analyze

```python
func.std(get_column(table, 'score'))

┌───────┐
│ 15.32 │
└───────┘
```

## Sintaxe SQL

```sql
STD(<score>)
```

## Exemplos SQL

```sql
SELECT STD(score) FROM test_results;

┌───────┐
│ 15.32 │
└───────┘
```
