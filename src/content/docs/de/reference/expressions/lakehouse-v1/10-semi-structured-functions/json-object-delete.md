---
title: JSON_OBJECT_DELETE (Lakehouse v1)
description: JSON_OBJECT_DELETE — Löscht angegebene Schlüssel aus einem JSON-Objekt und gibt das geänderte Objekt zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-delete.md
---

Löscht angegebene Schlüssel aus einem JSON-Objekt und gibt das geänderte Objekt zurück. Existiert ein angegebener Schlüssel im Objekt nicht, wird er ignoriert.

## SQL Syntax

```sql
json_object_delete(<json_object>, <key1> [, <key2>, ...])
```

## Parameters

| Parameter | Beschreibung |
|-----------|--------------|
| json_object | Ein JSON-Objekt (Typ VARIANT), aus dem Schlüssel gelöscht werden. |
| key1, key2, ... | Ein oder mehrere Zeichenfolgenliterale, die die Schlüssel angeben, die aus dem Objekt gelöscht werden. |

## Return Type

Gibt eine VARIANT zurück, die das geänderte JSON-Objekt ohne die angegebenen Schlüssel enthält.

## SQL Examples

Einen einzelnen Schlüssel löschen:
```sql
SELECT json_object_delete('{"a":1,"b":2,"c":3}'::VARIANT, 'a');
-- Result: {"b":2,"c":3}
```

Mehrere Schlüssel löschen:
```sql
SELECT json_object_delete('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 'c');
-- Result: {"b":2,"d":4}
```

Einen nicht vorhandenen Schlüssel löschen (der Schlüssel wird ignoriert):
```sql
SELECT json_object_delete('{"a":1,"b":2}'::VARIANT, 'x');
-- Result: {"a":1,"b":2}
```
