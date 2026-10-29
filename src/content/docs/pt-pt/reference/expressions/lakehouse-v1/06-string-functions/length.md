---
title: LENGTH (Lakehouse v1)
description: LENGTH — devolve o comprimento de uma cadeia de caracteres ou de um valor binário.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/length.md
---

Devolve o comprimento de uma cadeia de caracteres ou de um valor binário. No caso de cadeias de caracteres, o comprimento representa o número de caracteres, sendo cada caráter UTF-8 considerado um único caráter. Para dados binários, o comprimento corresponde ao número de bytes.

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

## Tipo de Retorno

BIGINT

## Exemplos SQL

```sql
SELECT LENGTH('Hello'), LENGTH_UTF8('Hello'), CHAR_LENGTH('Hello'), CHARACTER_LENGTH('Hello');

┌───────────────────────────────────────────────────────────────────────────────────────────┐
│ length('hello') │ length_utf8('hello') │ char_length('hello') │ character_length('hello') │
├─────────────────┼──────────────────────┼──────────────────────┼───────────────────────────┤
│               5 │                    5 │                    5 │                         5 │
└───────────────────────────────────────────────────────────────────────────────────────────┘
```
