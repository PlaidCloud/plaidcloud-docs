---
title: TO_BINARY (Lakehouse v2)
description: TO_BINARY — convierte una cadena VARCHAR en un valor binario según el formato binario especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/03-binary-functions/to-binary.md
---

Convierte una cadena VARCHAR en un valor binario según el formato binario especificado.

## Sintaxis de Analyze

```python
func.to_binary(<str>, <format>)
```

## Ejemplos de Analyze

```python
func.to_binary('Hello', 'utf8')

┌──────────┐
│ b'Hello'  │
└──────────┘
```

## Sintaxis de SQL

```sql
TO_BINARY(<str>, <format>)
```

## Ejemplos de SQL

```sql
SELECT TO_BINARY('Hello', 'utf8');

┌────────────┐
│ 48656C6C6F  │
└────────────┘
```
