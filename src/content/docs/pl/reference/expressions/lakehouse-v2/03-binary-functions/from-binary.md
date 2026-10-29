---
title: FROM_BINARY (Lakehouse v2)
description: FROM_BINARY — konwertuje wartość binarną na ciąg VARCHAR zgodnie z podanym formatem binarnym.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/03-binary-functions/from-binary.md
---

Konwertuje wartość binarną na ciąg VARCHAR zgodnie z podanym formatem binarnym.

## Składnia Analyze

```python
func.from_binary(<binary>, <format>)
```

## Przykłady Analyze

```python
func.from_binary(b'\x48\x65\x6c\x6c\x6f', 'utf8')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## Składnia SQL

```sql
FROM_BINARY(<binary>, <format>)
```

## Przykłady SQL

```sql
SELECT FROM_BINARY(X'48656C6C6F', 'utf8');

┌───────┐
│ Hello  │
└───────┘
```
