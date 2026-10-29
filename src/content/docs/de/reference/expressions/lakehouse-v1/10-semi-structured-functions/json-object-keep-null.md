---
title: JSON_OBJECT_KEEP_NULL (Lakehouse v1)
description: JSON_OBJECT_KEEP_NULL — Erstellt ein JSON-Objekt mit Schlüsseln und Werten.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-keep-null.md
---

Erstellt ein JSON-Objekt mit Schlüsseln und Werten.

- Die Argumente sind null oder mehr Schlüssel-Wert-Paare (die Schlüssel sind Zeichenfolgen, die Werte können beliebigen Typs sein).
- Ist ein Schlüssel NULL, wird das Schlüssel-Wert-Paar im resultierenden Objekt weggelassen. Ist dagegen ein Wert NULL, bleibt das Schlüssel-Wert-Paar erhalten.
- Die Schlüssel müssen voneinander verschieden sein, und ihre Reihenfolge im resultierenden JSON kann von der angegebenen Reihenfolge abweichen.
- `TRY_JSON_OBJECT_KEEP_NULL` gibt einen NULL-Wert zurück, wenn beim Erstellen des Objekts ein Fehler auftritt.

Siehe auch: JSON_OBJECT

## SQL Syntax

```sql
JSON_OBJECT_KEEP_NULL(key1, value1[, key2, value2[, ...]])

TRY_JSON_OBJECT_KEEP_NULL(key1, value1[, key2, value2[, ...]])
```

## Return Type

JSON-Objekt.

## SQL Examples

```sql
SELECT JSON_OBJECT_KEEP_NULL();
┌─────────────────────────┐
│ json_object_keep_null() │
├─────────────────────────┤
│ {}                      │
└─────────────────────────┘

SELECT JSON_OBJECT_KEEP_NULL('a', 3.14, 'b', 'xx', 'c', NULL);
┌────────────────────────────────────────────────────────┐
│ json_object_keep_null('a', 3.14, 'b', 'xx', 'c', null) │
├────────────────────────────────────────────────────────┤
│ {"a":3.14,"b":"xx","c":null}                           │
└────────────────────────────────────────────────────────┘

SELECT JSON_OBJECT_KEEP_NULL('fruits', ['apple', 'banana', 'orange'], 'vegetables', ['carrot', 'celery']);
┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ json_object_keep_null('fruits', ['apple', 'banana', 'orange'], 'vegetables', ['carrot', 'celery']) │
├────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ {"fruits":["apple","banana","orange"],"vegetables":["carrot","celery"]}                            │
└────────────────────────────────────────────────────────────────────────────────────────────────────┘

SELECT JSON_OBJECT_KEEP_NULL('key');
  |
1 | SELECT JSON_OBJECT_KEEP_NULL('key')
  |        ^^^^^^^^^^^^^^^^^^ The number of keys and values must be equal while evaluating function `json_object_keep_null('key')`


SELECT TRY_JSON_OBJECT_KEEP_NULL('key');
┌──────────────────────────────────┐
│ try_json_object_keep_null('key') │
├──────────────────────────────────┤
│ NULL                             │
└──────────────────────────────────┘
```
