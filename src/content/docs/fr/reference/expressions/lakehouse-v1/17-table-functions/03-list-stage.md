---
title: LIST_STAGE (Lakehouse v1)
description: LIST_STAGE — liste les fichiers d'un stage.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/03-list-stage.md
---

Liste les fichiers d'un stage. Cela vous permet de filtrer les fichiers d'un stage selon leur extension et d'obtenir des informations détaillées sur chacun d'eux. La fonction est similaire à la commande DDL LIST STAGE FILES, mais elle vous offre la souplesse de récupérer des informations précises sur les fichiers avec l'instruction SELECT, comme le nom du fichier, sa taille, son hachage MD5, son horodatage de dernière modification et son créateur, plutôt que toutes les informations.

## Syntaxe SQL

```sql
LIST_STAGE(
  LOCATION => '{ internalStage | externalStage | userStage }'
  [ PATTERN => '<regex_pattern>']
)
```

Où :

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

Consultez COPY INTO table.


## Exemples SQL

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
