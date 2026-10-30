---
title: TYPEOF (Lakehouse v1)
description: TYPEOF — la fonction TYPEOF sert à renvoyer le nom d'un type de données.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/typeof.md
---

La fonction TYPEOF sert à renvoyer le nom d'un type de données.

## Syntaxe Analyze

```python
func.typeof( <expr> )
```

## Exemples Analyze

```python
func.typeof(1)
┌──────────────────┐
│ func.typeof(1)   │
├──────────────────┤
│ INT              │
└──────────────────┘
```

## Syntaxe SQL

```sql
TYPEOF( <expr> )
```

## Arguments

| Arguments   | Description |
| ----------- | ----------- |
| `<expr>` | Toute expression. <br /> Il peut s'agir d'un nom de colonne, du résultat d'une autre fonction ou d'une opération mathématique.

## Type de retour

Chaîne

## Exemples SQL

```sql
SELECT typeof(1::INT);
┌──────────────────┐
│ typeof(1::Int32) │
├──────────────────┤
│ INT              │
└──────────────────┘
```
