---
title: JQ (Lakehouse v1)
description: JQ — funkcja JQ zwracająca zbiór wierszy, która umożliwia zastosowanie filtrów jq.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/jq.md
---

Funkcja JQ to funkcja SQL zwracająca zbiór wierszy, która umożliwia stosowanie filtrów [jq](https://jqlang.github.io/jq/) do danych JSON przechowywanych w kolumnach Variant. Za jej pomocą możesz przetwarzać dane JSON, stosując wskazany filtr jq i otrzymując wyniki w postaci zbioru wierszy.

## Składnia SQL

```sql
JQ (<jq_expression>, <json_data>)
```

| Parametr        | Opis                                                                                                                                                                                                                                                                                                                                                        |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `jq_expression` | Wyrażenie filtru `jq` określające, jak przetwarzać i przekształcać dane JSON przy użyciu składni `jq`. Wyrażenie to może wskazywać, jak wybierać, modyfikować i przetwarzać dane w obiektach i tablicach JSON. Informacje o składni, filtrach i funkcjach obsługiwanych przez jq znajdziesz w [podręczniku jq](https://jqlang.github.io/jq/manual/#basic-filters). |
| `json_data`     | Dane wejściowe w formacie JSON, które chcesz przetworzyć lub przekształcić za pomocą wyrażenia filtru `jq`. Może to być obiekt JSON, tablica lub dowolna inna prawidłowa struktura danych JSON.                                                                                                                                                              |

## Typ zwracany

Funkcja JQ zwraca zbiór wartości JSON, z których każda odpowiada elementowi przekształconego lub wyodrębnionego wyniku na podstawie `<jq_expression>`.

## Przykłady SQL

Na początek tworzymy tabelę o nazwie `customer_data` z kolumnami `id` i `profile`, gdzie `profile` jest typu JSON i przechowuje informacje o użytkownikach:

```sql
CREATE TABLE customer_data (
    id INT,
    profile JSON
);

INSERT INTO customer_data VALUES
    (1, '{"name": "Alice", "age": 30, "city": "New York"}'),
    (2, '{"name": "Bob", "age": 25, "city": "Los Angeles"}'),
    (3, '{"name": "Charlie", "age": 35, "city": "Chicago"}');
```

Ten przykład wyodrębnia wybrane pola z danych JSON:

```sql
SELECT
    id,
    jq('.name', profile) AS customer_name
FROM
    customer_data;

┌─────────────────────────────────────┐
│        id       │   customer_name   │
├─────────────────┼───────────────────┤
│               1 │ "Alice"           │
│               2 │ "Bob"             │
│               3 │ "Charlie"         │
└─────────────────────────────────────┘
```

Ten przykład wybiera identyfikator użytkownika oraz jego wiek zwiększony o 1:

```sql
SELECT
    id,
    jq('.age + 1', profile) AS updated_age
FROM
    customer_data;

┌─────────────────────────────────────┐
│        id       │    updated_age    │
├─────────────────┼───────────────────┤
│               1 │ 31                │
│               2 │ 26                │
│               3 │ 36                │
└─────────────────────────────────────┘
```

Ten przykład zamienia nazwy miast na wielkie litery:

```sql
SELECT
    id,
    jq('.city | ascii_upcase', profile) AS city_uppercase
FROM
    customer_data;

┌─────────────────────────────────────┐
│        id       │   city_uppercase  │
├─────────────────┼───────────────────┤
│               1 │ "NEW YORK"        │
│               2 │ "LOS ANGELES"     │
│               3 │ "CHICAGO"         │
└─────────────────────────────────────┘
```
