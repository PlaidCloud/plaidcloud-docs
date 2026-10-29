---
title: RIGHT (Lakehouse v1)
description: RIGHT — devolve os len caracteres mais à direita da cadeia de caracteres str, ou NULL se algum argumento for NULL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/right.md
---

Devolve os len caracteres mais à direita da cadeia de caracteres str, ou NULL se algum argumento for NULL.

## Sintaxe do Analyze

```python
func.right(<str>, <len>)
```

## Exemplos do Analyze

```python
func.right('foobarbar', 4)
┌────────────────────────────┐
│ func.right('foobarbar', 4) │
├────────────────────────────┤
│ rbar                       │
└────────────────────────────┘
```

## Sintaxe SQL

```sql
RIGHT(<str>, <len>);
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
SELECT RIGHT('foobarbar', 4);
┌───────────────────────┐
│ RIGHT('foobarbar', 4) │
├───────────────────────┤
│ rbar                  │
└───────────────────────┘
```
