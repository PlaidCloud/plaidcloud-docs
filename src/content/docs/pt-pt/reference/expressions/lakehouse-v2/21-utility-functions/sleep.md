---
title: SLEEP (Lakehouse v2)
description: SLEEP — suspende a execução durante um número especificado de segundos. Devolve 0 em caso de êxito.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/sleep.md
---

Suspende a execução durante um número especificado de segundos. Devolve 0 em caso de êxito.

## Sintaxe do Analyze

```python
func.sleep(<seconds>)
```

## Exemplos do Analyze

```python
func.sleep(1)

┌───┐
│ 0  │
└───┘
```

## Sintaxe SQL

```sql
SLEEP(<seconds>)
```

## Exemplos SQL

```sql
SELECT SLEEP(1);

┌───┐
│ 0  │
└───┘
```
