---
title: JSON_MAP_FILTER (Lakehouse v1)
description: JSON_MAP_FILTER — Filtert Schlüssel-Wert-Paare in einem JSON-Objekt anhand einer angegebenen Bedingung.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-map-filter.md
---

Filtert Schlüssel-Wert-Paare in einem JSON-Objekt anhand einer angegebenen Bedingung, die als Lambda-Ausdruck definiert wird.

## SQL Syntax

```sql
JSON_MAP_FILTER(<json_object>, (<key>, <value>) -> <condition>)
```

## Return Type

Gibt ein JSON-Objekt zurück, das nur die Schlüssel-Wert-Paare enthält, die die angegebene Bedingung erfüllen.

## SQL Examples

Dieses Beispiel extrahiert nur das Schlüssel-Wert-Paar `"status": "active"` aus dem JSON-Objekt und filtert die übrigen Felder heraus:

```sql
SELECT JSON_MAP_FILTER('{"status":"active", "user":"admin", "time":"2024-11-01"}'::VARIANT, (k, v) -> k = 'status') AS filtered_metadata;

┌─────────────────────┐
│  filtered_metadata  │
├─────────────────────┤
│ {"status":"active"} │
└─────────────────────┘
```
