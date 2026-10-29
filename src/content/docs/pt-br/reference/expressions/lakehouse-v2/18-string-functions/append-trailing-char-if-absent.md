---
title: APPEND_TRAILING_CHAR_IF_ABSENT (Lakehouse v2)
description: "Use a função de string APPEND_TRAILING_CHAR_IF_ABSENT no PlaidCloud Lakehouse. Acrescenta um caractere final a uma string caso ele ainda não esteja presente."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/append-trailing-char-if-absent.md
---

Acrescenta um caractere final a uma string caso ele ainda não esteja presente.

## Sintaxe do Analyze

```python
func.append_trailing_char_if_absent(<str>, <char>)
```

## Exemplos do Analyze

```python
func.append_trailing_char_if_absent('hello', '!')

┌──────────┐
│ 'hello!'  │
└──────────┘
```

## Sintaxe SQL

```sql
APPEND_TRAILING_CHAR_IF_ABSENT(<str>, <char>)
```

## Exemplos de SQL

```sql
SELECT APPEND_TRAILING_CHAR_IF_ABSENT('hello', '!');

┌────────┐
│ hello!  │
└────────┘
```
