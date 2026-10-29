---
title: TRANSLATE (Lakehouse v2)
description: TRANSLATE — Substitui caracteres de uma string com base em um mapeamento de caracteres.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/translate.md
---

Substitui caracteres de uma string com base em um mapeamento de caracteres.

## Sintaxe do Analyze

```python
func.translate(<str>, <from>, <to>)
```

## Exemplos do Analyze

```python
func.translate('hello', 'el', 'ip')

┌─────────┐
│ 'hippo'  │
└─────────┘
```

## Sintaxe SQL

```sql
TRANSLATE(<str>, <from>, <to>)
```

## Exemplos de SQL

```sql
SELECT TRANSLATE('hello', 'el', 'ip');

┌───────┐
│ hippo  │
└───────┘
```
