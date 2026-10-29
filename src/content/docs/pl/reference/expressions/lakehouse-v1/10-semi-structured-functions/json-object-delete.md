---
title: JSON_OBJECT_DELETE (Lakehouse v1)
description: JSON_OBJECT_DELETE — usuwa wskazane klucze z obiektu JSON i zwraca zmodyfikowany obiekt.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-delete.md
---

Usuwa wskazane klucze z obiektu JSON i zwraca zmodyfikowany obiekt. Jeśli wskazany klucz nie istnieje w obiekcie, jest ignorowany.

## Składnia SQL

```sql
json_object_delete(<json_object>, <key1> [, <key2>, ...])
```

## Parametry

| Parametr | Opis |
|-----------|-------------|
| json_object | Obiekt JSON (typ VARIANT), z którego usuwane są klucze. |
| key1, key2, ... | Jeden lub więcej literałów tekstowych reprezentujących klucze do usunięcia z obiektu. |

## Typ zwracany

Zwraca VARIANT zawierający zmodyfikowany obiekt JSON z usuniętymi wskazanymi kluczami.

## Przykłady SQL

Usunięcie pojedynczego klucza:
```sql
SELECT json_object_delete('{"a":1,"b":2,"c":3}'::VARIANT, 'a');
-- Result: {"b":2,"c":3}
```

Usunięcie wielu kluczy:
```sql
SELECT json_object_delete('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 'c');
-- Result: {"b":2,"d":4}
```

Usunięcie nieistniejącego klucza (klucz jest ignorowany):
```sql
SELECT json_object_delete('{"a":1,"b":2}'::VARIANT, 'x');
-- Result: {"a":1,"b":2}
```
