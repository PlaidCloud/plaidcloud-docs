---
title: TO_BINARY (Lakehouse v2)
description: TO_BINARY — converte uma string VARCHAR em um valor binário com base no formato binário especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/03-binary-functions/to-binary.md
---

Converte uma string VARCHAR em um valor binário com base no formato binário especificado.

## Sintaxe do Analyze

```python
func.to_binary(<str>, <format>)
```

## Exemplos do Analyze

```python
func.to_binary('Hello', 'utf8')

┌──────────┐
│ b'Hello'  │
└──────────┘
```

## Sintaxe SQL

```sql
TO_BINARY(<str>, <format>)
```

## Exemplos SQL

```sql
SELECT TO_BINARY('Hello', 'utf8');

┌────────────┐
│ 48656C6C6F  │
└────────────┘
```
