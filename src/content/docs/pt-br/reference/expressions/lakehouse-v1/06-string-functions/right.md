---
title: RIGHT (Lakehouse v1)
description: RIGHT — retorna os len caracteres mais à direita da string str, ou NULL se algum argumento for NULL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/right.md
---

Retorna os len caracteres mais à direita da string str, ou NULL se algum argumento for NULL.

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

| Argumentos | Descrição                                                  |
|-----------|-------------------------------------------------------------|
| `<str>`   | A string principal da qual os caracteres serão extraídos    |
| `<len>`   | A quantidade de caracteres                                  |

## Tipo de retorno

`VARCHAR`

## Exemplos de SQL

```sql
SELECT RIGHT('foobarbar', 4);
┌───────────────────────┐
│ RIGHT('foobarbar', 4) │
├───────────────────────┤
│ rbar                  │
└───────────────────────┘
```
