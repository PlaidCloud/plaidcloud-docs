---
title: DICT_GET (Lakehouse v1)
description: DICT_GET — recupera o valor de um atributo especificado de um dicionário usando uma expressão de chave informada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/19-dictionary-functions/dict-get.md
---

Recupera o valor de um atributo especificado de um dicionário usando uma expressão de chave informada.

## Sintaxe SQL

```sql
DICT_GET([db_name.]<dict_name>, '<attr_name>', <key_expr>)
```

| Parâmetro | Descrição                                                                                                                                                         |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dict_name | O nome do dicionário.                                                                                                                                             |
| attr_name | O nome do atributo do dicionário cujo valor você deseja recuperar.                                                                                                |
| key_expr  | A expressão de chave usada para localizar uma entrada específica no dicionário. Representa o valor da chave primária do dicionário para recuperar os dados correspondentes. |

## Exemplos de SQL
