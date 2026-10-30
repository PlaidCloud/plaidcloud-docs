---
title: POSITION (Lakehouse v1)
description: POSITION — POSITION(substr IN str) é um sinônimo de LOCATE(substr,str).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/position.md
---

POSITION(substr IN str) é um sinônimo de LOCATE(substr,str).
Retorna a posição da primeira ocorrência da substring substr na string str.
Retorna 0 se substr não estiver em str. Retorna NULL se algum argumento for NULL.

## Sintaxe do Analyze

```python
func.position(<substr>, <str>)
```

## Exemplos do Analyze

```python
func.position('bar', 'foobarbar')
┌───────────────────────────────────┐
│ func.position('bar', 'foobarbar') │
├───────────────────────────────────┤
│                                 4 │
└───────────────────────────────────┘
```

## Sintaxe SQL

```sql
POSITION(<substr> IN <str>)
```

## Argumentos

| Argumentos | Descrição       |
|------------|-----------------|
| `<substr>` | A substring.    |
| `<str>`    | A string.       |

## Tipo de retorno

`BIGINT`

## Exemplos de SQL

```sql
SELECT POSITION('bar' IN 'foobarbar')
┌────────────────────────────┐
│ POSITION('bar' IN 'foobarbar') │
├────────────────────────────┤
│                          4 │
└────────────────────────────┘

SELECT POSITION('xbar' IN 'foobar')
┌──────────────────────────┐
│ POSITION('xbar' IN 'foobar') │
├──────────────────────────┤
│                        0 │
└──────────────────────────┘
```
