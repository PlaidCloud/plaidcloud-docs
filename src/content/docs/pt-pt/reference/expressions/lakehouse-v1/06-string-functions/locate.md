---
title: LOCATE (Lakehouse v1)
description: LOCATE — a primeira sintaxe devolve a posição da primeira ocorrência da subcadeia substr na cadeia de caracteres str.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/locate.md
---

A primeira sintaxe devolve a posição da primeira ocorrência da subcadeia substr na cadeia de caracteres str.
A segunda sintaxe devolve a posição da primeira ocorrência da subcadeia substr na cadeia de caracteres str, a partir da posição pos.
Devolve 0 se substr não existir em str. Devolve NULL se algum argumento for NULL.

## Sintaxe do Analyze

```python
func.locate(<substr>, <str>, <pos>)
```

## Exemplos do Analyze

```python
func.locate('bar', 'foobarbar')
┌────────────────────────────────────┐
│ func.locate('bar', 'foobarbar') │
├────────────────────────────────────┤
│                                  5 │
└────────────────────────────────────┘
```

```python
func.locate('bar', 'foobarbar', 5)
┌────────────────────────────────────┐
│ func.locate('bar', 'foobarbar', 5) │
├────────────────────────────────────┤
│                                  7 │
└────────────────────────────────────┘
```

## Sintaxe SQL

```sql
LOCATE(<substr>, <str>)
LOCATE(<substr>, <str>, <pos>)
```

## Argumentos

| Argumentos | Descrição               |
|------------|-------------------------|
| `<substr>` | A subcadeia.            |
| `<str>`    | A cadeia de caracteres. |
| `<pos>`    | A posição.              |

## Tipo de Retorno

`BIGINT`

## Exemplos SQL

```sql
SELECT LOCATE('bar', 'foobarbar')
┌────────────────────────────┐
│ LOCATE('bar', 'foobarbar') │
├────────────────────────────┤
│                          4 │
└────────────────────────────┘

SELECT LOCATE('xbar', 'foobar')
┌──────────────────────────┐
│ LOCATE('xbar', 'foobar') │
├──────────────────────────┤
│                        0 │
└──────────────────────────┘

SELECT LOCATE('bar', 'foobarbar', 5)
┌───────────────────────────────┐
│ LOCATE('bar', 'foobarbar', 5) │
├───────────────────────────────┤
│                             7 │
└───────────────────────────────┘
```
