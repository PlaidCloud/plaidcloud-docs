---
title: DICT_GET (Lakehouse v1)
description: DICT_GET — pobiera wartość wskazanego atrybutu ze słownika przy użyciu podanego wyrażenia klucza.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/19-dictionary-functions/dict-get.md
---

Pobiera wartość wskazanego atrybutu ze słownika przy użyciu podanego wyrażenia klucza.

## Składnia SQL

```sql
DICT_GET([db_name.]<dict_name>, '<attr_name>', <key_expr>)
```

| Parametr | Opis                                                                                                                                                       |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dict_name | Nazwa słownika.                                                                                                                                       |
| attr_name | Nazwa atrybutu w słowniku, którego wartość chcesz pobrać.                                                                              |
| key_expr  | Wyrażenie klucza służące do zlokalizowania konkretnego wpisu w słowniku. Reprezentuje wartość klucza głównego słownika, aby pobrać odpowiadające mu dane. |

## Przykłady SQL
