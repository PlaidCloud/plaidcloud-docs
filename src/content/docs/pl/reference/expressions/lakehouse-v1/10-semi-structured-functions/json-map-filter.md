---
title: JSON_MAP_FILTER (Lakehouse v1)
description: JSON_MAP_FILTER — filtruje pary klucz-wartość w obiekcie JSON na podstawie określonego warunku.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-map-filter.md
---

Filtruje pary klucz-wartość w obiekcie JSON na podstawie określonego warunku, zdefiniowanego za pomocą wyrażenia lambda.

## Składnia SQL

```sql
JSON_MAP_FILTER(<json_object>, (<key>, <value>) -> <condition>)
```

## Typ zwracany

Zwraca obiekt JSON zawierający wyłącznie pary klucz-wartość spełniające określony warunek.

## Przykłady SQL

Ten przykład wyodrębnia z obiektu JSON tylko parę klucz-wartość `"status": "active"`, odfiltrowując pozostałe pola:

```sql
SELECT JSON_MAP_FILTER('{"status":"active", "user":"admin", "time":"2024-11-01"}'::VARIANT, (k, v) -> k = 'status') AS filtered_metadata;

┌─────────────────────┐
│  filtered_metadata  │
├─────────────────────┤
│ {"status":"active"} │
└─────────────────────┘
```
