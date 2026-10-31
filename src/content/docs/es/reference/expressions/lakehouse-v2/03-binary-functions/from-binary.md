---
title: FROM_BINARY (Lakehouse v2)
description: FROM_BINARY — convierte un valor binario en una cadena VARCHAR según el formato binario especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/03-binary-functions/from-binary.md
---

Convierte un valor binario en una cadena VARCHAR según el formato binario especificado.

## Sintaxis de Analyze

```python
func.from_binary(<binary>, <format>)
```

## Ejemplos de Analyze

```python
func.from_binary(b'\x48\x65\x6c\x6c\x6f', 'utf8')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## Sintaxis de SQL

```sql
FROM_BINARY(<binary>, <format>)
```

## Ejemplos de SQL

```sql
SELECT FROM_BINARY(X'48656C6C6F', 'utf8');

┌───────┐
│ Hello  │
└───────┘
```
