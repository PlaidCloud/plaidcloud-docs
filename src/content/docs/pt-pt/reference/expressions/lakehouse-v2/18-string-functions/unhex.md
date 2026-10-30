---
title: UNHEX (Lakehouse v2)
description: UNHEX — converte uma cadeia hexadecimal numa cadeia de carateres.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/unhex.md
---

Converte uma cadeia hexadecimal numa cadeia de carateres.

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

## Exemplos SQL

```sql
SELECT UNHEX('48656C6C6F');

┌───────┐
│ Hello  │
└───────┘
```
