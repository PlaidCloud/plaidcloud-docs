---
title: JSON_MAP_TRANSFORM_KEYS (Lakehouse v1)
description: JSON_MAP_TRANSFORM_KEYS — stosuje przekształcenie do każdego klucza w obiekcie JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-map-transform-keys.md
---

Stosuje przekształcenie do każdego klucza w obiekcie JSON za pomocą wyrażenia lambda.

## Składnia SQL

```sql
JSON_MAP_TRANSFORM_KEYS(<json_object>, (<key>, <value>) -> <key_transformation>)
```

## Typ zwracany

Zwraca obiekt JSON z tymi samymi wartościami co wejściowy obiekt JSON, ale z kluczami zmodyfikowanymi zgodnie z podanym przekształceniem lambda.

## Przykłady SQL

Ten przykład dopisuje „_v1” do każdego klucza, tworząc nowy obiekt JSON ze zmodyfikowanymi kluczami:

```sql
SELECT JSON_MAP_TRANSFORM_KEYS('{"name":"John", "role":"admin"}'::VARIANT, (k, v) -> CONCAT(k, '_v1')) AS versioned_metadata;

┌──────────────────────────────────────┐
│          versioned_metadata          │
├──────────────────────────────────────┤
│ {"name_v1":"John","role_v1":"admin"} │
└──────────────────────────────────────┘
```
