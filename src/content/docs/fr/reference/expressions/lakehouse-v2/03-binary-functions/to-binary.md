---
title: TO_BINARY (Lakehouse v2)
description: TO_BINARY — convertit une chaîne VARCHAR en valeur binaire selon le format binaire indiqué.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/03-binary-functions/to-binary.md
---

Convertit une chaîne VARCHAR en valeur binaire selon le format binaire indiqué.

## Syntaxe Analyze

```python
func.to_binary(<str>, <format>)
```

## Exemples Analyze

```python
func.to_binary('Hello', 'utf8')

┌──────────┐
│ b'Hello'  │
└──────────┘
```

## Syntaxe SQL

```sql
TO_BINARY(<str>, <format>)
```

## Exemples SQL

```sql
SELECT TO_BINARY('Hello', 'utf8');

┌────────────┐
│ 48656C6C6F  │
└────────────┘
```
