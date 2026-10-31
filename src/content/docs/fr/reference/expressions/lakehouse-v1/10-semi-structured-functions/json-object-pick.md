---
title: JSON_OBJECT_PICK (Lakehouse v1)
description: JSON_OBJECT_PICK — crée un nouvel objet JSON ne contenant que les clés spécifiées.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-pick.md
---

Crée un nouvel objet JSON ne contenant que les clés spécifiées de l'objet JSON en entrée. Si une clé spécifiée n'existe pas dans l'objet en entrée, elle est omise du résultat.

## Syntaxe SQL

```sql
json_object_pick(<json_object>, <key1> [, <key2>, ...])
```

## Paramètres

| Paramètre | Description |
|-----------|-------------|
| json_object | Un objet JSON (type VARIANT) dont les clés doivent être sélectionnées. |
| key1, key2, ... | Un ou plusieurs littéraux de type chaîne représentant les clés à inclure dans l'objet résultat. |

## Type de retour

Renvoie un VARIANT contenant un nouvel objet JSON avec uniquement les clés spécifiées et leurs valeurs correspondantes.

## Exemples SQL

Sélectionner une seule clé :
```sql
SELECT json_object_pick('{"a":1,"b":2,"c":3}'::VARIANT, 'a');
-- Result: {"a":1}
```

Sélectionner plusieurs clés :
```sql
SELECT json_object_pick('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 'b');
-- Result: {"a":1,"b":2}
```

Sélectionner avec une clé inexistante (les clés inexistantes sont ignorées) :
```sql
SELECT json_object_pick('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 'c');
-- Result: {"a":1}
```
