---
title: REVERSE (Lakehouse v1)
description: REVERSE — retorna a string str com a ordem dos caracteres invertida.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/reverse.md
---

Retorna a string str com a ordem dos caracteres invertida.

## Sintaxe do Analyze

```python
func.reverse(<str>)
```

## Exemplos do Analyze

```python
func.reverse('abc')
┌──────────────────────┐
│ func..reverse('abc') │
├──────────────────────┤
│ cba                  │
└──────────────────────┘
```

## Sintaxe SQL

```sql
REVERSE(<str>)
```

## Argumentos

| Argumentos | Descrição            |
|-----------|----------------------|
| `<str>`   | O valor da string.   |

## Tipo de retorno

`VARCHAR`

## Exemplos de SQL

```sql
SELECT REVERSE('abc');
┌────────────────┐
│ REVERSE('abc') │
├────────────────┤
│ cba            │
└────────────────┘
```
