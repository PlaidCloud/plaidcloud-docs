---
title: INSPECT_PARQUET (Lakehouse v1)
description: INSPECT_PARQUET — pobiera tabelę z kompleksowymi metadanymi pliku Parquet znajdującego się w obszarze przejściowym.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/02-inspect-parquet.md
---

Pobiera tabelę z kompleksowymi metadanymi pliku Parquet znajdującego się w obszarze przejściowym (stage), zawierającą następujące kolumny:

| Kolumna                           | Opis                                                    |
|----------------------------------|----------------------------------------------------------------|
| created_by                       | Podmiot lub źródło odpowiedzialne za utworzenie pliku Parquet |
| num_columns                      | Liczba kolumn w pliku Parquet                      |
| num_rows                         | Łączna liczba wierszy lub rekordów w pliku Parquet        |
| num_row_groups                   | Liczba grup wierszy w pliku Parquet                |
| serialized_size                  | Rozmiar pliku Parquet na dysku (po kompresji)              |
| max_row_groups_size_compressed   | Rozmiar największej grupy wierszy (po kompresji)                 |
| max_row_groups_size_uncompressed | Rozmiar największej grupy wierszy (bez kompresji)               |

## Składnia SQL

```sql
INSPECT_PARQUET('@<path-to-file>')
```

## Przykłady SQL

Ten przykład pobiera metadane z przykładowego pliku Parquet o nazwie [books.parquet](https://datafuse-1253727613.cos.ap-hongkong.myqcloud.com/data/books.parquet), znajdującego się w obszarze przejściowym. Plik zawiera dwa rekordy:

```text title='books.parquet'
Transaction Processing,Jim Gray,1992
Readings in Database Systems,Michael Stonebraker,2004
```

```sql
-- Show the staged file
LIST @my_internal_stage;

┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│      name     │  size  │        md5       │         last_modified         │      creator     │
├───────────────┼────────┼──────────────────┼───────────────────────────────┼──────────────────┤
│ books.parquet │    998 │ NULL             │ 2023-04-19 19:34:51.303 +0000 │ NULL             │
└──────────────────────────────────────────────────────────────────────────────────────────────┘

-- Retrieve metadata from the staged file
SELECT * FROM INSPECT_PARQUET('@my_internal_stage/books.parquet');

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│             created_by             │ num_columns │ num_rows │ num_row_groups │ serialized_size │ max_row_groups_size_compressed │ max_row_groups_size_uncompressed │
├────────────────────────────────────┼─────────────┼──────────┼────────────────┼─────────────────┼────────────────────────────────┼──────────────────────────────────┤
│ parquet-cpp version 1.5.1-SNAPSHOT │           3 │        2 │              1 │             998 │                            332 │                              320 │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
