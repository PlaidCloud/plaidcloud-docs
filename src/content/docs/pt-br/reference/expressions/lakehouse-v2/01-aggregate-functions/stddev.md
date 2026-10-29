---
title: STDDEV (Lakehouse v2)
description: STDDEV — retorna o desvio padrão populacional. Alias de `STDDEV_POP`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/stddev.md
---

Retorna o desvio padrão populacional. Alias de `STDDEV_POP`.

## Sintaxe do Analyze

```python
func.stddev(get_column(table, 'score'))
```

## Exemplos do Analyze

```python
func.stddev(get_column(table, 'score'))

┌───────┐
│ 15.32 │
└───────┘
```

## Sintaxe SQL

```sql
STDDEV(<score>)
```

## Exemplos SQL

```sql
SELECT STDDEV(score) FROM test_results;

┌───────┐
│ 15.32 │
└───────┘
```
