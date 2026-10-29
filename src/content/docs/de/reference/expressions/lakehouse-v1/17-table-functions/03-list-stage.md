---
title: LIST_STAGE (Lakehouse v1)
description: LIST_STAGE listet die Dateien in einem Stage auf.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/03-list-stage.md
---

Listet die Dateien in einem Stage auf. Damit können Sie Dateien in einem Stage anhand ihrer Erweiterungen filtern und umfassende Details zu jeder Datei abrufen. Die Funktion ähnelt dem DDL-Befehl LIST STAGE FILES, bietet Ihnen aber die Flexibilität, mit der SELECT-Anweisung gezielt bestimmte Dateiinformationen abzurufen, etwa Dateiname, Größe, MD5-Hash, Zeitstempel der letzten Änderung und Ersteller, statt aller Dateiinformationen.

## SQL-Syntax

```sql
LIST_STAGE(
  LOCATION => '{ internalStage | externalStage | userStage }'
  [ PATTERN => '<regex_pattern>']
)
```

Dabei gilt:

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

Siehe COPY INTO table.


## SQL-Beispiele

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
