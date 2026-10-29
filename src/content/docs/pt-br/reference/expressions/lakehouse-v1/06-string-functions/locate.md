---
title: LOCATE (Lakehouse v1)
description: LOCATE — a primeira sintaxe retorna a posição da primeira ocorrência da substring substr na string str.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/locate.md
---

A primeira sintaxe retorna a posição da primeira ocorrência da substring substr na string str.
A segunda sintaxe retorna a posição da primeira ocorrência da substring substr na string str, a partir da posição pos.
Retorna 0 se substr não estiver em str. Retorna NULL se algum argumento for NULL.

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

| Argumentos | Descrição         |
|------------|-------------------|
| `<substr>` | A substring.      |
| `<str>`    | A string.         |
| `<pos>`    | A posição.        |

## Tipo de retorno

`BIGINT`

## Exemplos de SQL

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
