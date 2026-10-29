---
title: LIST_STAGE (Lakehouse v1)
description: LIST_STAGE — wyświetla pliki w obszarze przejściowym (stage).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/03-list-stage.md
---

Wyświetla pliki w obszarze przejściowym (stage). Pozwala filtrować pliki w obszarze na podstawie ich rozszerzeń i uzyskać szczegółowe informacje o każdym pliku. Funkcja jest podobna do polecenia DDL LIST STAGE FILES, ale umożliwia pobranie wybranych informacji o plikach za pomocą instrukcji SELECT, takich jak nazwa pliku, rozmiar, skrót MD5, sygnatura czasowa ostatniej modyfikacji i twórca, zamiast wszystkich informacji o pliku.

## Składnia SQL

```sql
LIST_STAGE(
  LOCATION => '{ internalStage | externalStage | userStage }'
  [ PATTERN => '<regex_pattern>']
)
```

Gdzie:

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

Zobacz COPY INTO table.


## Przykłady SQL

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
