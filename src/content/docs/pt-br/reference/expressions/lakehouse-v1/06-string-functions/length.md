---
title: LENGTH (Lakehouse v1)
description: LENGTH — retorna o comprimento de uma string ou valor binário informado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/length.md
---

Retorna o comprimento de uma string ou valor binário informado. No caso de strings, o comprimento representa a contagem de caracteres, com cada caractere UTF-8 considerado um único caractere. Para dados binários, o comprimento corresponde ao número de bytes.

## Sintaxe do Analyze

```python
func.length(<expr>)
```

## Exemplos do Analyze

```python
func.length('Hello')
┌──────────────────────┐
│ func.length('Hello') │
├──────────────────────┤
│                    5 │
└──────────────────────┘
```

## Sintaxe SQL

```sql
LENGTH(<expr>)
```

## Aliases

- [CHAR_LENGTH](../char-length)
- [CHARACTER_LENGTH](../character-length)
- [LENGTH_UTF8](../length-utf8)

## Tipo de retorno

BIGINT

## Exemplos de SQL

```sql
SELECT LENGTH('Hello'), LENGTH_UTF8('Hello'), CHAR_LENGTH('Hello'), CHARACTER_LENGTH('Hello');

┌───────────────────────────────────────────────────────────────────────────────────────────┐
│ length('hello') │ length_utf8('hello') │ char_length('hello') │ character_length('hello') │
├─────────────────┼──────────────────────┼──────────────────────┼───────────────────────────┤
│               5 │                    5 │                    5 │                         5 │
└───────────────────────────────────────────────────────────────────────────────────────────┘
```
