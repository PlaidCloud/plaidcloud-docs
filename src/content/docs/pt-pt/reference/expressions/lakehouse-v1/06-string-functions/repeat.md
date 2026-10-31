---
title: REPEAT (Lakehouse v1)
description: REPEAT — devolve uma cadeia de caracteres composta pela cadeia str repetida count vezes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/repeat.md
---

Devolve uma cadeia de caracteres composta pela cadeia str repetida count vezes. Se count for inferior a 1, devolve uma cadeia de caracteres vazia. Devolve NULL se str ou count forem NULL.

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

| Argumentos | Descrição               |
|-----------|-------------------------|
| `<str>`   | A cadeia de caracteres. |
| `<count>` | O número.               |

## Exemplos SQL

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
