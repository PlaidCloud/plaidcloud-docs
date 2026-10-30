---
title: LIST_STAGE (Lakehouse v1)
description: LIST_STAGE enumera los archivos de una etapa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/03-list-stage.md
---

Enumera los archivos de una etapa. Le permite filtrar los archivos de una etapa según su extensión y obtener información detallada de cada archivo. La función es similar al comando DDL LIST STAGE FILES, pero le ofrece la flexibilidad de recuperar con la sentencia SELECT información específica de los archivos, como el nombre, el tamaño, el hash MD5, la marca de tiempo de la última modificación y el creador, en lugar de toda la información del archivo.

## Sintaxis de SQL

```sql
LIST_STAGE(
  LOCATION => '{ internalStage | externalStage | userStage }'
  [ PATTERN => '<regex_pattern>']
)
```

Donde:

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


## Ejemplos de SQL

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
