---
title: REPEAT (Lakehouse v1)
description: REPEAT — retorna uma string formada pela string str repetida count vezes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/repeat.md
---

Retorna uma string formada pela string str repetida count vezes. Se count for menor que 1, retorna uma string vazia. Retorna NULL se str ou count for NULL.

## Sintaxe do Analyze

```python
func.repeat(<str>, <count>)
```

## Exemplos do Analyze

```python
func.repeat(<str>, <count>)
┌─────────────────────────┐
│ func.repeat('plaid', 3) │
├─────────────────────────┤
│ plaidplaidplaid         │
└─────────────────────────┘
```

## Sintaxe SQL

```sql
REPEAT(<str>, <count>)
```

## Argumentos

| Argumentos | Descrição  |
|-----------|-------------|
| `<str>`   | A string.   |
| `<count>` | O número.   |

## Exemplos de SQL

```sql
SELECT REPEAT('databend', 3);
┌──────────────────────────┐
│ REPEAT('databend', 3)    │
├──────────────────────────┤
│ databenddatabenddatabend │
└──────────────────────────┘

SELECT REPEAT('databend', 0);
┌───────────────────────┐
│ REPEAT('databend', 0) │
├───────────────────────┤
│                       │
└───────────────────────┘

SELECT REPEAT('databend', NULL);
┌──────────────────────────┐
│ REPEAT('databend', NULL) │
├──────────────────────────┤
│                     NULL │
└──────────────────────────┘
```
