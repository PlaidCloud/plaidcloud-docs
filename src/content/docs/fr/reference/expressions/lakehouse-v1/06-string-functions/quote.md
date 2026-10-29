---
title: QUOTE (Lakehouse v1)
description: QUOTE met une chaîne entre guillemets pour produire un résultat utilisable comme valeur de données correctement échappée dans une instruction SQL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/quote.md
---

Met une chaîne entre guillemets pour produire un résultat utilisable comme valeur de données correctement échappée dans une instruction SQL. 

## Syntaxe Analyze

```python
func.quote(<str>)
```

## Exemples Analyze

```python
func.quote('Don\'t')
┌──────────────────────┐
│ func.quote('Don\'t') │
├──────────────────────┤
│  Don\'t!             │
└──────────────────────┘
```

## Syntaxe SQL

```sql
QUOTE(<str>)
```

## Exemples SQL

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
