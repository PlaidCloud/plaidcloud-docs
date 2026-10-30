---
title: JSON_MAP_TRANSFORM_KEYS (Lakehouse v1)
description: JSON_MAP_TRANSFORM_KEYS — Wendet eine Transformation auf jeden Schlüssel in einem JSON-Objekt an.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-map-transform-keys.md
---

Wendet mit einem Lambda-Ausdruck eine Transformation auf jeden Schlüssel in einem JSON-Objekt an.

## SQL Syntax

```sql
JSON_MAP_TRANSFORM_KEYS(<json_object>, (<key>, <value>) -> <key_transformation>)
```

## Return Type

Gibt ein JSON-Objekt mit denselben Werten wie das JSON-Eingabeobjekt zurück, dessen Schlüssel jedoch gemäß der angegebenen Lambda-Transformation geändert wurden.

## SQL Examples

Dieses Beispiel hängt „_v1“ an jeden Schlüssel an und erstellt so ein neues JSON-Objekt mit geänderten Schlüsseln:

```sql
SELECT JSON_MAP_TRANSFORM_KEYS('{"name":"John", "role":"admin"}'::VARIANT, (k, v) -> CONCAT(k, '_v1')) AS versioned_metadata;

┌──────────────────────────────────────┐
│          versioned_metadata          │
├──────────────────────────────────────┤
│ {"name_v1":"John","role_v1":"admin"} │
└──────────────────────────────────────┘
```
