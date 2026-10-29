---
title: JSON_OBJECT_PICK (Lakehouse v1)
description: JSON_OBJECT_PICK — tworzy nowy obiekt JSON zawierający wyłącznie wskazane klucze.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-pick.md
---

Tworzy nowy obiekt JSON zawierający wyłącznie wskazane klucze z wejściowego obiektu JSON. Jeśli wskazany klucz nie istnieje w obiekcie wejściowym, jest pomijany w wyniku.

## Składnia SQL

```sql
json_object_pick(<json_object>, <key1> [, <key2>, ...])
```

## Parametry

| Parametr | Opis |
|-----------|-------------|
| json_object | Obiekt JSON (typ VARIANT), z którego wybierane są klucze. |
| key1, key2, ... | Jeden lub więcej literałów tekstowych reprezentujących klucze, które mają się znaleźć w obiekcie wynikowym. |

## Typ zwracany

Zwraca VARIANT zawierający nowy obiekt JSON tylko ze wskazanymi kluczami i odpowiadającymi im wartościami.

## Przykłady SQL

Wybranie pojedynczego klucza:
```sql
SELECT json_object_pick('{"a":1,"b":2,"c":3}'::VARIANT, 'a');
-- Result: {"a":1}
```

Wybranie wielu kluczy:
```sql
SELECT json_object_pick('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 'b');
-- Result: {"a":1,"b":2}
```

Wybranie z nieistniejącym kluczem (nieistniejące klucze są ignorowane):
```sql
SELECT json_object_pick('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 'c');
-- Result: {"a":1}
```
