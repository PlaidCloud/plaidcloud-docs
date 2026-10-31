---
title: POSITION (Lakehouse v1)
description: POSITION — POSITION(substr IN str) é sinónimo de LOCATE(substr,str).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/position.md
---

POSITION(substr IN str) é sinónimo de LOCATE(substr,str).
Devolve a posição da primeira ocorrência da subcadeia substr na cadeia de caracteres str.
Devolve 0 se substr não existir em str. Devolve NULL se algum argumento for NULL.

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

| Argumentos | Descrição               |
|------------|-------------------------|
| `<substr>` | A subcadeia.            |
| `<str>`    | A cadeia de caracteres. |

## Tipo de Retorno

`BIGINT`

## Exemplos SQL

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
