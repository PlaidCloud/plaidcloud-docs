---
title: LENGTH (Lakehouse v1)
description: LENGTH — devuelve la longitud de una cadena o un valor binario de entrada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/length.md
---

Devuelve la longitud de una cadena o un valor binario de entrada. En el caso de las cadenas, la longitud representa el número de caracteres, y cada carácter UTF-8 se cuenta como un solo carácter. En el caso de los datos binarios, la longitud corresponde al número de bytes.

## Sintaxis de Analyze

```python
func.length(<expr>)
```

## Ejemplos de Analyze

```python
func.length('Hello')
┌──────────────────────┐
│ func.length('Hello') │
├──────────────────────┤
│                    5 │
└──────────────────────┘
```

## Sintaxis SQL

```sql
LENGTH(<expr>)
```

## Alias

- [CHAR_LENGTH](../char-length)
- [CHARACTER_LENGTH](../character-length)
- [LENGTH_UTF8](../length-utf8)

## Tipo de retorno

BIGINT

## Ejemplos de SQL

```sql
SELECT LENGTH('Hello'), LENGTH_UTF8('Hello'), CHAR_LENGTH('Hello'), CHARACTER_LENGTH('Hello');

┌───────────────────────────────────────────────────────────────────────────────────────────┐
│ length('hello') │ length_utf8('hello') │ char_length('hello') │ character_length('hello') │
├─────────────────┼──────────────────────┼──────────────────────┼───────────────────────────┤
│               5 │                    5 │                    5 │                         5 │
└───────────────────────────────────────────────────────────────────────────────────────────┘
```
