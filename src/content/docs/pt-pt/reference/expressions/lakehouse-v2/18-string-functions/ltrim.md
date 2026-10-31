---
title: LTRIM (Lakehouse v2)
description: LTRIM — remove os espaços em branco iniciais ou os carateres especificados do início de uma cadeia.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ltrim.md
---

Remove os espaços em branco iniciais ou os carateres especificados do início de uma cadeia.

## Sintaxe do Analyze

```python
func.ltrim(<str>)
```

## Exemplos do Analyze

```python
func.ltrim('   hello')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## Sintaxe SQL

```sql
LTRIM(<str>)
```

## Exemplos SQL

```sql
SELECT LTRIM('   hello');

┌───────┐
│ hello  │
└───────┘
```
