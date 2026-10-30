---
title: UNHEX (Lakehouse v2)
description: UNHEX — converte uma string hexadecimal em uma string de caracteres.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/unhex.md
---

Converte uma string hexadecimal em uma string de caracteres.

## Sintaxe do Analyze

```python
func.unhex(<hex_str>)
```

## Exemplos do Analyze

```python
func.unhex('48656C6C6F')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## Sintaxe SQL

```sql
UNHEX(<hex_str>)
```

## Exemplos de SQL

```sql
SELECT UNHEX('48656C6C6F');

┌───────┐
│ Hello  │
└───────┘
```
