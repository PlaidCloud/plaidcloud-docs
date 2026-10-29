---
title: JSON_OBJECT_INSERT (Lakehouse v1)
description: JSON_OBJECT_INSERT — Fügt in einem JSON-Objekt ein Schlüssel-Wert-Paar ein oder aktualisiert es.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-insert.md
---

Fügt in einem JSON-Objekt ein Schlüssel-Wert-Paar ein oder aktualisiert es.

## SQL Syntax

```sql
JSON_OBJECT_INSERT(<json_object>, <key>, <value>[, <update_flag>])
```

| Parameter           | Beschreibung | |
|---------------------|--------------|---|
| `<json_object>`     | Das JSON-Eingabeobjekt. | |
| `<key>`             | Der Schlüssel, der eingefügt oder aktualisiert wird. | |
| `<value>`           | Der Wert, der dem Schlüssel zugewiesen wird. | |
| `<update_flag>` | Ein Boolescher Schalter, der steuert, ob der Wert ersetzt wird, wenn der angegebene Schlüssel im JSON-Objekt bereits vorhanden ist. Bei `true` ersetzt die Funktion den Wert, wenn der Schlüssel bereits vorhanden ist. Bei `false` (oder wenn der Schalter fehlt) tritt ein Fehler auf, wenn der Schlüssel vorhanden ist. | |

## Return Type

Gibt das aktualisierte JSON-Objekt zurück.

## SQL Examples

Dieses Beispiel zeigt, wie Sie einen neuen Schlüssel 'c' mit dem Wert 3 in das vorhandene JSON-Objekt einfügen:

```sql
SELECT JSON_OBJECT_INSERT('{"a":1,"b":2,"d":4}'::variant, 'c', 3);

┌────────────────────────────────────────────────────────────┐
│ json_object_insert('{"a":1,"b":2,"d":4}'::VARIANT, 'c', 3) │
├────────────────────────────────────────────────────────────┤
│ {"a":1,"b":2,"c":3,"d":4}                                  │
└────────────────────────────────────────────────────────────┘
```

Dieses Beispiel zeigt, wie Sie den Wert des vorhandenen Schlüssels 'a' von 1 auf 10 aktualisieren: Der Aktualisierungsschalter ist auf `true` gesetzt, sodass der Wert des Schlüssels ersetzt werden darf:

```sql
SELECT JSON_OBJECT_INSERT('{"a":1,"b":2,"d":4}'::variant, 'a', 10, true);

┌───────────────────────────────────────────────────────────────────┐
│ json_object_insert('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 10, TRUE) │
├───────────────────────────────────────────────────────────────────┤
│ {"a":10,"b":2,"d":4}                                              │
└───────────────────────────────────────────────────────────────────┘
```

Dieses Beispiel zeigt den Fehler, der auftritt, wenn Sie versuchen, einen Wert für den vorhandenen Schlüssel 'a' einzufügen, ohne den Aktualisierungsschalter auf `true` zu setzen:

```sql
SELECT JSON_OBJECT_INSERT('{"a":1,"b":2,"d":4}'::variant, 'a', 10);

error: APIError: ResponseError with 1006: ObjectDuplicateKey while evaluating function `json_object_insert('{"a":1,"b":2,"d":4}', 'a', 10)` in expr `json_object_insert('{"a":1,"b":2,"d":4}', 'a', 10)`
```
