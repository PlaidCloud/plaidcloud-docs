---
title: DICT_GET (Lakehouse v1)
description: DICT_GET — obtém o valor de um atributo especificado de um dicionário através de uma expressão de chave fornecida.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/19-dictionary-functions/dict-get.md
---

Obtém o valor de um atributo especificado de um dicionário através de uma expressão de chave fornecida.

## Sintaxe SQL

```sql
DICT_GET([db_name.]<dict_name>, '<attr_name>', <key_expr>)
```

| Parâmetro | Descrição                                                                                                                                                       |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dict_name | O nome do dicionário.                                                                                                                                       |
| attr_name | O nome do atributo do dicionário cujo valor pretende obter.                                                                              |
| key_expr  | A expressão de chave utilizada para localizar uma entrada específica no dicionário. Representa o valor da chave primária do dicionário para obter os dados correspondentes. |

## Exemplos de SQL
