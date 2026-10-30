---
title: QUOTE (Lakehouse v1)
description: QUOTE — coloca uma string entre aspas para produzir um resultado que pode ser usado como valor de dados corretamente escapado em uma instrução SQL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/quote.md
---

Coloca uma string entre aspas para produzir um resultado que pode ser usado como valor de dados corretamente escapado em uma instrução SQL. 

## Sintaxe do Analyze

```python
func.quote(<str>)
```

## Exemplos do Analyze

```python
func.quote('Don\'t')
┌──────────────────────┐
│ func.quote('Don\'t') │
├──────────────────────┤
│  Don\'t!             │
└──────────────────────┘
```

## Sintaxe SQL

```sql
QUOTE(<str>)
```

## Exemplos de SQL

```sql
SELECT QUOTE('Don\'t!');
┌─────────────────┐
│ QUOTE('Don't!') │
├─────────────────┤
│ Don\'t!         │
└─────────────────┘

SELECT QUOTE(NULL);
┌─────────────┐
│ QUOTE(NULL) │
├─────────────┤
│        NULL │
└─────────────┘
```
