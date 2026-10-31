---
title: APPEND_TRAILING_CHAR_IF_ABSENT (Lakehouse v2)
description: "Utilize a função de cadeia APPEND_TRAILING_CHAR_IF_ABSENT no PlaidCloud Lakehouse. Acrescenta um caráter final a uma cadeia se este ainda não estiver presente."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/append-trailing-char-if-absent.md
---

Acrescenta um caráter final a uma cadeia se este ainda não estiver presente.

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

## Exemplos SQL

```sql
SELECT APPEND_TRAILING_CHAR_IF_ABSENT('hello', '!');

┌────────┐
│ hello!  │
└────────┘
```
