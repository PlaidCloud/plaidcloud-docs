---
title: DICT_GET (Lakehouse v1)
description: DICT_GET recupera el valor de un atributo especificado de un diccionario mediante una expresión de clave proporcionada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/19-dictionary-functions/dict-get.md
---

Recupera el valor de un atributo especificado de un diccionario mediante una expresión de clave proporcionada.

## Sintaxis de SQL

```sql
DICT_GET([db_name.]<dict_name>, '<attr_name>', <key_expr>)
```

| Parámetro | Descripción                                                                                                                                                       |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dict_name | El nombre del diccionario.                                                                                                                                        |
| attr_name | El nombre del atributo del diccionario cuyo valor desea recuperar.                                                                                                |
| key_expr  | La expresión de clave que se usa para localizar una entrada específica del diccionario. Representa el valor de la clave principal del diccionario para recuperar los datos correspondientes. |

## Ejemplos de SQL
