---
title: LEFT (Lakehouse v1)
description: LEFT — retorna os len caracteres mais à esquerda da string str, ou NULL se algum argumento for NULL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/left.md
---

Retorna os len caracteres mais à esquerda da string str, ou NULL se algum argumento for NULL.

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

| Argumentos | Descrição                                                  |
|-----------|-------------------------------------------------------------|
| `<str>`   | A string principal da qual os caracteres serão extraídos    |
| `<len>`   | A quantidade de caracteres                                  |

## Tipo de retorno

`VARCHAR`

## Exemplos de SQL

```sql
SELECT LEFT('foobarbar', 5);
┌──────────────────────┐
│ LEFT('foobarbar', 5) │
├──────────────────────┤
│ fooba                │
└──────────────────────┘
```
