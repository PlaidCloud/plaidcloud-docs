---
title: DICT_GET (Lakehouse v1)
description: DICT_GET — récupère la valeur d'un attribut spécifié d'un dictionnaire à l'aide d'une expression de clé fournie.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/19-dictionary-functions/dict-get.md
---

Récupère la valeur d'un attribut spécifié d'un dictionnaire à l'aide d'une expression de clé fournie.

## Syntaxe SQL

```sql
DICT_GET([db_name.]<dict_name>, '<attr_name>', <key_expr>)
```

| Paramètre | Description                                                                                                                                                       |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dict_name | Le nom du dictionnaire.                                                                                                                                           |
| attr_name | Le nom de l'attribut du dictionnaire dont vous voulez récupérer la valeur.                                                                                        |
| key_expr  | L'expression de clé utilisée pour localiser une entrée précise du dictionnaire. Elle représente la valeur de la clé primaire du dictionnaire permettant de récupérer les données correspondantes. |

## Exemples SQL
