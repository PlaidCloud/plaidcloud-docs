---
title: LEFT (Lakehouse v1)
description: LEFT — devolve os len caracteres mais à esquerda da cadeia de caracteres str, ou NULL se algum argumento for NULL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/left.md
---

Devolve os len caracteres mais à esquerda da cadeia de caracteres str, ou NULL se algum argumento for NULL.

## Sintaxe do Analyze

```python
func.left(<str>, <len>)
```

## Exemplos do Analyze

```python
func.left('foobarbar', 5)
┌───────────────────────────┐
│ func.left('foobarbar', 5) │
├───────────────────────────┤
│ fooba                     │
└───────────────────────────┘
```

## Sintaxe SQL

```sql
LEFT(<str>, <len>);
```

## Argumentos

| Argumentos | Descrição                                                              |
|-----------|------------------------------------------------------------------------|
| `<str>`   | A cadeia de caracteres principal de onde os caracteres vão ser extraídos |
| `<len>`   | O número de caracteres                                                 |

## Tipo de Retorno

`VARCHAR`

## Exemplos SQL

```sql
SELECT LEFT('foobarbar', 5);
┌──────────────────────┐
│ LEFT('foobarbar', 5) │
├──────────────────────┤
│ fooba                │
└──────────────────────┘
```
