---
title: CHAR_LENGTH (Lakehouse v2)
description: CHAR_LENGTH — devolve o número de carateres de uma cadeia.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/char-length.md
---

Devolve o número de carateres de uma cadeia.

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

## Exemplos SQL

```sql
SELECT CHAR_LENGTH('hello world');

┌────┐
│ 11  │
└────┘
```
