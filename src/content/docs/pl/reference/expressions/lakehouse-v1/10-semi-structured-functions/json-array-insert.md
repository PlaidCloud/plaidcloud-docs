---
title: JSON_ARRAY_INSERT (Lakehouse v1)
description: JSON_ARRAY_INSERT — wstawia wartość do tablicy JSON pod wskazanym indeksem i zwraca zaktualizowaną tablicę JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-insert.md
---

Wstawia wartość do tablicy JSON pod wskazanym indeksem i zwraca zaktualizowaną tablicę JSON.

## Składnia SQL

```sql
JSON_ARRAY_INSERT(<json_array>, <index>, <json_value>)
```

| Parametr       | Opis                                                                                                                                                                                                     |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<json_array>` | Tablica JSON do zmodyfikowania.                                                                                                                                                                          |
| `<index>`      | Pozycja, na której zostanie wstawiona wartość. Indeksy dodatnie wstawiają wartość na wskazanej pozycji lub dołączają ją na końcu, jeśli indeks wykracza poza zakres; indeksy ujemne wstawiają wartość licząc od końca lub na początku, jeśli indeks wykracza poza zakres. |
| `<json_value>` | Wartość JSON do wstawienia do tablicy.                                                                                                                                                                   |

## Typ zwracany

Tablica JSON.

## Przykłady SQL

Gdy `<index>` jest nieujemną liczbą całkowitą, nowy element jest wstawiany na wskazanej pozycji, a istniejące elementy są przesuwane w prawo.

```sql
-- The new element is inserted at position 0 (the beginning of the array), shifting all original elements to the right
SELECT JSON_ARRAY_INSERT('["task1", "task2", "task3"]'::VARIANT, 0, '"new_task"'::VARIANT);

-[ RECORD 1 ]-----------------------------------
json_array_insert('["task1", "task2", "task3"]'::VARIANT, 0, '"new_task"'::VARIANT): ["new_task","task1","task2","task3"]

-- The new element is inserted at position 1, between task1 and task2
SELECT JSON_ARRAY_INSERT('["task1", "task2", "task3"]'::VARIANT, 1, '"new_task"'::VARIANT);

-[ RECORD 1 ]-----------------------------------
json_array_insert('["task1", "task2", "task3"]'::VARIANT, 1, '"new_task"'::VARIANT): ["task1","new_task","task2","task3"]

-- If the index exceeds the length of the array, the new element is appended at the end of the array
SELECT JSON_ARRAY_INSERT('["task1", "task2", "task3"]'::VARIANT, 6, '"new_task"'::VARIANT);

-[ RECORD 1 ]-----------------------------------
json_array_insert('["task1", "task2", "task3"]'::VARIANT, 6, '"new_task"'::VARIANT): ["task1","task2","task3","new_task"]
```

Ujemny `<index>` jest liczony od końca tablicy: `-1` oznacza pozycję przed ostatnim elementem, `-2` przed przedostatnim i tak dalej.

```sql
-- The new element is inserted just before the last element (task3)
SELECT JSON_ARRAY_INSERT('["task1", "task2", "task3"]'::VARIANT, -1, '"new_task"'::VARIANT);

-[ RECORD 1 ]-----------------------------------
json_array_insert('["task1", "task2", "task3"]'::VARIANT, - 1, '"new_task"'::VARIANT): ["task1","task2","new_task","task3"]

-- Since the negative index exceeds the array’s length, the new element is inserted at the beginning
SELECT JSON_ARRAY_INSERT('["task1", "task2", "task3"]'::VARIANT, -6, '"new_task"'::VARIANT);

-[ RECORD 1 ]-----------------------------------
json_array_insert('["task1", "task2", "task3"]'::VARIANT, - 6, '"new_task"'::VARIANT): ["new_task","task1","task2","task3"]
```
