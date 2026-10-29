---
title: APPEND_TRAILING_CHAR_IF_ABSENT (Lakehouse v2)
description: "Użyj funkcji tekstowej APPEND_TRAILING_CHAR_IF_ABSENT w PlaidCloud Lakehouse. Dołącza na końcu ciągu znak końcowy, jeśli jeszcze go tam nie ma."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/append-trailing-char-if-absent.md
---

Dołącza na końcu ciągu znak końcowy, jeśli jeszcze go tam nie ma.

## Składnia Analyze

```python
func.append_trailing_char_if_absent(<str>, <char>)
```

## Przykłady Analyze

```python
func.append_trailing_char_if_absent('hello', '!')

┌──────────┐
│ 'hello!'  │
└──────────┘
```

## Składnia SQL

```sql
APPEND_TRAILING_CHAR_IF_ABSENT(<str>, <char>)
```

## Przykłady SQL

```sql
SELECT APPEND_TRAILING_CHAR_IF_ABSENT('hello', '!');

┌────────┐
│ hello!  │
└────────┘
```
