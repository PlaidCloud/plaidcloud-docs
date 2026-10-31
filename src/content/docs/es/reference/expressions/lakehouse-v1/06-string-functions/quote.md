---
title: QUOTE (Lakehouse v1)
description: QUOTE — entrecomilla una cadena para producir un resultado que se pueda usar como valor de datos correctamente escapado en una instrucción SQL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/quote.md
---

Entrecomilla una cadena para producir un resultado que se pueda usar como valor de datos correctamente escapado en una instrucción SQL. 

## Sintaxis de Analyze

```python
func.quote(<str>)
```

## Ejemplos de Analyze

```python
func.quote('Don\'t')
┌──────────────────────┐
│ func.quote('Don\'t') │
├──────────────────────┤
│  Don\'t!             │
└──────────────────────┘
```

## Sintaxis SQL

```sql
QUOTE(<str>)
```

## Ejemplos de SQL

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
