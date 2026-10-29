---
title: DICT_GET (Lakehouse v1)
description: DICT_GET ruft den Wert eines angegebenen Attributs aus einem Dictionary mithilfe eines bereitgestellten Schlüsselausdrucks ab.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/19-dictionary-functions/dict-get.md
---

Ruft den Wert eines angegebenen Attributs aus einem Dictionary mithilfe eines bereitgestellten Schlüsselausdrucks ab.

## SQL-Syntax

```sql
DICT_GET([db_name.]<dict_name>, '<attr_name>', <key_expr>)
```

| Parameter | Beschreibung                                                                                                                                                       |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dict_name | Der Name des Dictionarys.                                                                                                                                       |
| attr_name | Der Name des Attributs im Dictionary, dessen Wert Sie abrufen möchten.                                                                              |
| key_expr  | Der Schlüsselausdruck, mit dem ein bestimmter Eintrag im Dictionary gefunden wird. Er steht für den Wert des Primärschlüssels des Dictionarys, um die zugehörigen Daten abzurufen. |

## SQL-Beispiele
