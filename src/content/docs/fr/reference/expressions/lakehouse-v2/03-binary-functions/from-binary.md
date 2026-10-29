---
title: FROM_BINARY (Lakehouse v2)
description: FROM_BINARY — convertit une valeur binaire en chaîne VARCHAR selon le format binaire indiqué.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/03-binary-functions/from-binary.md
---

Convertit une valeur binaire en chaîne VARCHAR selon le format binaire indiqué.

## Syntaxe Analyze

```python
func.from_binary(<binary>, <format>)
```

## Exemples Analyze

```python
func.from_binary(b'\x48\x65\x6c\x6c\x6f', 'utf8')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## Syntaxe SQL

```sql
FROM_BINARY(<binary>, <format>)
```

## Exemples SQL

```sql
SELECT FROM_BINARY(X'48656C6C6F', 'utf8');

┌───────┐
│ Hello  │
└───────┘
```
