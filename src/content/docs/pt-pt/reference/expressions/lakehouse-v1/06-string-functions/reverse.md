---
title: REVERSE (Lakehouse v1)
description: REVERSE — devolve a cadeia de caracteres str com a ordem dos caracteres invertida.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/reverse.md
---

Devolve a cadeia de caracteres str com a ordem dos caracteres invertida.

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

| Argumentos | Descrição                          |
|-----------|------------------------------------|
| `<str>`   | O valor da cadeia de caracteres.   |

## Tipo de Retorno

`VARCHAR`

## Exemplos SQL

```sql
SELECT REVERSE('abc');
┌────────────────┐
│ REVERSE('abc') │
├────────────────┤
│ cba            │
└────────────────┘
```
