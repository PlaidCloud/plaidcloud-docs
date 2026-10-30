---
title: LIST_STAGE (Lakehouse v1)
description: LIST_STAGE — lista os ficheiros de uma área de preparação.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/03-list-stage.md
---

Lista os ficheiros de uma área de preparação. Permite filtrar os ficheiros de uma área de preparação com base nas respetivas extensões e obter detalhes completos sobre cada ficheiro. A função é semelhante ao comando DDL LIST STAGE FILES, mas oferece a flexibilidade de obter informação específica dos ficheiros com a instrução SELECT, como o nome do ficheiro, o tamanho, o hash MD5, a data e hora da última modificação e o criador, em vez de toda a informação dos ficheiros.

## Sintaxe SQL

```sql
LIST_STAGE(
  LOCATION => '{ internalStage | externalStage | userStage }'
  [ PATTERN => '<regex_pattern>']
)
```

Onde:

### Internalstage

```sql
internalStage ::= @<internal_stage_name>[/<path>]
```

### Externalstage

```sql
externalStage ::= @<external_stage_name>[/<path>]
```

### Userstage

```sql
userStage ::= @~[/<path>]
```

### PATTERN

Consulte COPY INTO table.


## Exemplos de SQL

```sql
SELECT * FROM list_stage(location => '@my_stage/', pattern => '.*[.]log');
┌────────────────┬──────┬────────────────────────────────────┬───────────────────────────────┬─────────┐
│      name      │ size │                md5                 │         last_modified         │ creator │
├────────────────┼──────┼────────────────────────────────────┼───────────────────────────────┼─────────┤
│ 2023/meta.log  │  475 │ "4208ff530b252236e14b3cd797abdfbd" │ 2023-04-19 20:23:24.000 +0000 │ NULL    │
│ 2023/query.log │ 1348 │ "1c6654b207472c277fc8c6207c035e18" │ 2023-04-19 20:23:24.000 +0000 │ NULL    │
└────────────────┴──────┴────────────────────────────────────┴───────────────────────────────┴─────────┘

-- Equivalent to the following statement:
LIST @my_stage PATTERN = '.log';
```
