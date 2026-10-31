---
title: JSON_OBJECT_INSERT (Lakehouse v1)
description: JSON_OBJECT_INSERT — insère ou met à jour une paire clé-valeur dans un objet JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-insert.md
---

Insère ou met à jour une paire clé-valeur dans un objet JSON.

## Syntaxe SQL

```sql
JSON_OBJECT_INSERT(<json_object>, <key>, <value>[, <update_flag>])
```

| Paramètre           | Description                                                                                                                                                                                                                                          |   |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| `<json_object>`     | L'objet JSON en entrée.                                                                                                                                                                                                                              |   |
| `<key>`             | La clé à insérer ou à mettre à jour.                                                                                                                                                                                                                 |   |
| `<value>`           | La valeur à affecter à la clé.                                                                                                                                                                                                                       |   |
| `<update_flag>` | Un indicateur booléen qui détermine si la valeur est remplacée lorsque la clé spécifiée existe déjà dans l'objet JSON. Si `true`, la fonction remplace la valeur lorsque la clé existe déjà. Si `false` (ou omis), une erreur se produit lorsque la clé existe. |   |

## Type de retour

Renvoie l'objet JSON mis à jour.

## Exemples SQL

Cet exemple montre comment insérer une nouvelle clé « c » avec la valeur 3 dans l'objet JSON existant :

```sql
SELECT JSON_OBJECT_INSERT('{"a":1,"b":2,"d":4}'::variant, 'c', 3);

┌────────────────────────────────────────────────────────────┐
│ json_object_insert('{"a":1,"b":2,"d":4}'::VARIANT, 'c', 3) │
├────────────────────────────────────────────────────────────┤
│ {"a":1,"b":2,"c":3,"d":4}                                  │
└────────────────────────────────────────────────────────────┘
```

Cet exemple montre comment faire passer de 1 à 10 la valeur de la clé existante « a » en définissant l'indicateur de mise à jour sur `true`, ce qui autorise le remplacement de la valeur de la clé :

```sql
SELECT JSON_OBJECT_INSERT('{"a":1,"b":2,"d":4}'::variant, 'a', 10, true);

┌───────────────────────────────────────────────────────────────────┐
│ json_object_insert('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 10, TRUE) │
├───────────────────────────────────────────────────────────────────┤
│ {"a":10,"b":2,"d":4}                                              │
└───────────────────────────────────────────────────────────────────┘
```

Cet exemple illustre l'erreur qui se produit lorsque l'on tente d'insérer une valeur pour la clé existante « a » sans définir l'indicateur de mise à jour sur `true` :

```sql
SELECT JSON_OBJECT_INSERT('{"a":1,"b":2,"d":4}'::variant, 'a', 10);

error: APIError: ResponseError with 1006: ObjectDuplicateKey while evaluating function `json_object_insert('{"a":1,"b":2,"d":4}', 'a', 10)` in expr `json_object_insert('{"a":1,"b":2,"d":4}', 'a', 10)`
```
