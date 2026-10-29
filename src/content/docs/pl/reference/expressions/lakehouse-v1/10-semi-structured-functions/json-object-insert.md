---
title: JSON_OBJECT_INSERT (Lakehouse v1)
description: JSON_OBJECT_INSERT — wstawia lub aktualizuje parę klucz-wartość w obiekcie JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-insert.md
---

Wstawia lub aktualizuje parę klucz-wartość w obiekcie JSON.

## Składnia SQL

```sql
JSON_OBJECT_INSERT(<json_object>, <key>, <value>[, <update_flag>])
```

| Parametr            | Opis                                                                                                                                                                                                                                                 |   |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| `<json_object>`     | Wejściowy obiekt JSON.                                                                                                                                                                                                                               |   |
| `<key>`             | Klucz do wstawienia lub zaktualizowania.                                                                                                                                                                                                             |   |
| `<value>`           | Wartość przypisywana do klucza.                                                                                                                                                                                                                      |   |
| `<update_flag>` | Flaga logiczna określająca, czy zastąpić wartość, jeśli wskazany klucz już istnieje w obiekcie JSON. Jeśli `true`, funkcja zastępuje wartość, gdy klucz już istnieje. Jeśli `false` (lub pominięto), wystąpi błąd, gdy klucz istnieje. |   |

## Typ zwracany

Zwraca zaktualizowany obiekt JSON.

## Przykłady SQL

Ten przykład pokazuje, jak wstawić do istniejącego obiektu JSON nowy klucz „c” z wartością 3:

```sql
SELECT JSON_OBJECT_INSERT('{"a":1,"b":2,"d":4}'::variant, 'c', 3);

┌────────────────────────────────────────────────────────────┐
│ json_object_insert('{"a":1,"b":2,"d":4}'::VARIANT, 'c', 3) │
├────────────────────────────────────────────────────────────┤
│ {"a":1,"b":2,"c":3,"d":4}                                  │
└────────────────────────────────────────────────────────────┘
```

Ten przykład pokazuje, jak zaktualizować wartość istniejącego klucza „a” z 1 na 10, ustawiając flagę aktualizacji na `true`, co pozwala zastąpić wartość klucza:

```sql
SELECT JSON_OBJECT_INSERT('{"a":1,"b":2,"d":4}'::variant, 'a', 10, true);

┌───────────────────────────────────────────────────────────────────┐
│ json_object_insert('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 10, TRUE) │
├───────────────────────────────────────────────────────────────────┤
│ {"a":10,"b":2,"d":4}                                              │
└───────────────────────────────────────────────────────────────────┘
```

Ten przykład pokazuje błąd, który występuje przy próbie wstawienia wartości dla istniejącego klucza „a” bez ustawienia flagi aktualizacji na `true`:

```sql
SELECT JSON_OBJECT_INSERT('{"a":1,"b":2,"d":4}'::variant, 'a', 10);

error: APIError: ResponseError with 1006: ObjectDuplicateKey while evaluating function `json_object_insert('{"a":1,"b":2,"d":4}', 'a', 10)` in expr `json_object_insert('{"a":1,"b":2,"d":4}', 'a', 10)`
```
