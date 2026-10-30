---
title: CHAR_LENGTH (Lakehouse v2)
description: CHAR_LENGTH — retorna o número de caracteres de uma string.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/char-length.md
---

Retorna o número de caracteres de uma string.

## Sintaxe do Analyze

```python
func.char_length(<str>)
```

## Exemplos do Analyze

```python
func.char_length('hello world')

┌────┐
│ 11  │
└────┘
```

## Sintaxe SQL

```sql
CHAR_LENGTH(<str>)
```

## Exemplos de SQL

```sql
SELECT CHAR_LENGTH('hello world');

┌────┐
│ 11  │
└────┘
```
