---
title: CURRENT_USER (Lakehouse v1)
description: CURRENT_USER — renvoie la combinaison nom d'utilisateur et nom d'hôte du compte que le serveur.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/current-user.md
---

Renvoie la combinaison nom d'utilisateur et nom d'hôte du compte que le serveur a utilisé pour authentifier le client actuel. Ce compte détermine vos privilèges d'accès. La valeur renvoyée est une chaîne dans le jeu de caractères utf8.

## Syntaxe Analyze

```python
func.current_user()
```

## Exemples Analyze

```python
func.current_user()

┌─────────────────────┐
│ func.current_user() │
├─────────────────────┤
│ 'root'@'%'          │
└─────────────────────┘
```

## Syntaxe SQL

```sql
CURRENT_USER()
```

## Exemples SQL

```sql
SELECT CURRENT_USER();

┌────────────────┐
│ current_user() │
├────────────────┤
│ 'root'@'%'     │
└────────────────┘
```
