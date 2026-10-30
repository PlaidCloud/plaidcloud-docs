---
title: JSON_OBJECT_DELETE (Lakehouse v1)
description: JSON_OBJECT_DELETE — supprime les clés spécifiées d'un objet JSON et renvoie l'objet modifié.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-delete.md
---

Supprime les clés spécifiées d'un objet JSON et renvoie l'objet modifié. Si une clé spécifiée n'existe pas dans l'objet, elle est ignorée.

## Syntaxe SQL

```sql
json_object_delete(<json_object>, <key1> [, <key2>, ...])
```

## Paramètres

| Paramètre | Description |
|-----------|-------------|
| json_object | Un objet JSON (type VARIANT) dont les clés doivent être supprimées. |
| key1, key2, ... | Un ou plusieurs littéraux de type chaîne représentant les clés à supprimer de l'objet. |

## Type de retour

Renvoie un VARIANT contenant l'objet JSON modifié, sans les clés spécifiées.

## Exemples SQL

Supprimer une seule clé :
```sql
SELECT json_object_delete('{"a":1,"b":2,"c":3}'::VARIANT, 'a');
-- Result: {"b":2,"c":3}
```

Supprimer plusieurs clés :
```sql
SELECT json_object_delete('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 'c');
-- Result: {"b":2,"d":4}
```

Supprimer une clé inexistante (la clé est ignorée) :
```sql
SELECT json_object_delete('{"a":1,"b":2}'::VARIANT, 'x');
-- Result: {"a":1,"b":2}
```
