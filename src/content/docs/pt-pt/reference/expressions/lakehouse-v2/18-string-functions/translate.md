---
title: TRANSLATE (Lakehouse v2)
description: TRANSLATE — substitui carateres numa cadeia com base num mapeamento de carateres.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/translate.md
---

Substitui carateres numa cadeia com base num mapeamento de carateres.

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

## Exemplos SQL

```sql
SELECT TRANSLATE('hello', 'el', 'ip');

┌───────┐
│ hippo  │
└───────┘
```
