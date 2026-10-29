---
title: JSON_OBJECT_PICK (Lakehouse v1)
description: JSON_OBJECT_PICK — Erstellt ein neues JSON-Objekt, das nur die angegebenen Schlüssel enthält.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-pick.md
---

Erstellt ein neues JSON-Objekt, das nur die angegebenen Schlüssel des JSON-Eingabeobjekts enthält. Existiert ein angegebener Schlüssel im Eingabeobjekt nicht, wird er im Ergebnis weggelassen.

## SQL Syntax

```sql
json_object_pick(<json_object>, <key1> [, <key2>, ...])
```

## Parameters

| Parameter | Beschreibung |
|-----------|--------------|
| json_object | Ein JSON-Objekt (Typ VARIANT), aus dem Schlüssel ausgewählt werden. |
| key1, key2, ... | Ein oder mehrere Zeichenfolgenliterale, die die Schlüssel angeben, die in das Ergebnisobjekt aufgenommen werden. |

## Return Type

Gibt eine VARIANT zurück, die ein neues JSON-Objekt mit nur den angegebenen Schlüsseln und ihren zugehörigen Werten enthält.

## SQL Examples

Einen einzelnen Schlüssel auswählen:
```sql
SELECT json_object_pick('{"a":1,"b":2,"c":3}'::VARIANT, 'a');
-- Result: {"a":1}
```

Mehrere Schlüssel auswählen:
```sql
SELECT json_object_pick('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 'b');
-- Result: {"a":1,"b":2}
```

Auswahl mit einem nicht vorhandenen Schlüssel (nicht vorhandene Schlüssel werden ignoriert):
```sql
SELECT json_object_pick('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 'c');
-- Result: {"a":1}
```
