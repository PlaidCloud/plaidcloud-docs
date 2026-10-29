---
title: FROM_BINARY (Lakehouse v2)
description: FROM_BINARY — converte um valor binário numa cadeia VARCHAR com base no formato binário especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/03-binary-functions/from-binary.md
---

Converte um valor binário numa cadeia VARCHAR com base no formato binário especificado.

## Sintaxe do Analyze

```python
func.from_binary(<binary>, <format>)
```

## Exemplos do Analyze

```python
func.from_binary(b'\x48\x65\x6c\x6c\x6f', 'utf8')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## Sintaxe SQL

```sql
FROM_BINARY(<binary>, <format>)
```

## Exemplos SQL

```sql
SELECT FROM_BINARY(X'48656C6C6F', 'utf8');

┌───────┐
│ Hello  │
└───────┘
```
