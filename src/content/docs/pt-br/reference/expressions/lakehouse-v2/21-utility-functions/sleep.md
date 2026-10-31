---
title: SLEEP (Lakehouse v2)
description: SLEEP — pausa a execução por um número especificado de segundos. Retorna 0 em caso de sucesso.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/sleep.md
---

Pausa a execução por um número especificado de segundos. Retorna 0 em caso de sucesso.

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

## Exemplos de SQL

```sql
SELECT SLEEP(1);

┌───┐
│ 0  │
└───┘
```
