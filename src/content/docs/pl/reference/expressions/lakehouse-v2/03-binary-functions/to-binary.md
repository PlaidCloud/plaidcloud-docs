---
title: TO_BINARY (Lakehouse v2)
description: TO_BINARY — konwertuje ciąg VARCHAR na wartość binarną zgodnie z podanym formatem binarnym.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/03-binary-functions/to-binary.md
---

Konwertuje ciąg VARCHAR na wartość binarną zgodnie z podanym formatem binarnym.

## Składnia Analyze

```python
func.to_binary(<str>, <format>)
```

## Przykłady Analyze

```python
func.to_binary('Hello', 'utf8')

┌──────────┐
│ b'Hello'  │
└──────────┘
```

## Składnia SQL

```sql
TO_BINARY(<str>, <format>)
```

## Przykłady SQL

```sql
SELECT TO_BINARY('Hello', 'utf8');

┌────────────┐
│ 48656C6C6F  │
└────────────┘
```
