---
title: STRCMP (Lakehouse v1)
description: STRCMP — retorna 0 se as strings forem iguais, -1 se o primeiro argumento for menor que o segundo e 1 nos demais casos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/strcmp.md
---

Retorna 0 se as strings forem iguais, -1 se o primeiro argumento for menor que o segundo e 1 nos demais casos.

## Sintaxe do Analyze

```python
func.strcmp(<expr1> ,<expr2>)
```

## Exemplos do Analyze

```python
func.strcmp('text', 'text2')
┌──────────────────────────────┐
│ func.strcmp('text', 'text2') │
├──────────────────────────────┤
│                           -1 │
└──────────────────────────────┘

func.strcmp('text2', 'text')
┌──────────────────────────────┐
│ func.strcmp('text2', 'text') │
├──────────────────────────────┤
│                            1 │
└──────────────────────────────┘

func.strcmp('text', 'text')
┌──────────────────────────────┐
│ func.strcmp('text', 'text')  │
├──────────────────────────────┤
│                            0 │
└──────────────────────────────┘
```

## Sintaxe SQL

```sql
STRCMP(<expr1> ,<expr2>)
```

## Argumentos

| Argumentos | Descrição |
|-----------|-------------|
| `<expr1>` | A string.   |
| `<expr2>` | A string.   |

## Tipo de retorno

`BIGINT`

## Exemplos de SQL

```sql
SELECT STRCMP('text', 'text2');
┌─────────────────────────┐
│ STRCMP('text', 'text2') │
├─────────────────────────┤
│                      -1 │
└─────────────────────────┘

SELECT STRCMP('text2', 'text');
┌─────────────────────────┐
│ STRCMP('text2', 'text') │
├─────────────────────────┤
│                       1 │
└─────────────────────────┘

SELECT STRCMP('text', 'text');
┌────────────────────────┐
│ STRCMP('text', 'text') │
├────────────────────────┤
│                      0 │
└────────────────────────┘
```
