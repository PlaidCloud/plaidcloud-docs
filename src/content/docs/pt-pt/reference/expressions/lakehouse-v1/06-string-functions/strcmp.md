---
title: STRCMP (Lakehouse v1)
description: STRCMP — devolve 0 se as cadeias de caracteres forem iguais, -1 se o primeiro argumento for menor do que o segundo e 1 caso contrário.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/strcmp.md
---

Devolve 0 se as cadeias de caracteres forem iguais, -1 se o primeiro argumento for menor do que o segundo e 1 caso contrário.

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

| Argumentos | Descrição               |
|-----------|-------------------------|
| `<expr1>` | A cadeia de caracteres. |
| `<expr2>` | A cadeia de caracteres. |

## Tipo de Retorno

`BIGINT`

## Exemplos SQL

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
