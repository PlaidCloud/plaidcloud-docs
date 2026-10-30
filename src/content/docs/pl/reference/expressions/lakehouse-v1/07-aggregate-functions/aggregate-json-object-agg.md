---
title: JSON_OBJECT_AGG (Lakehouse v1)
description: JSON_OBJECT_AGG — konwertuje pary klucz-wartość na obiekt JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-json-object-agg.md
---

Konwertuje pary klucz-wartość na obiekt JSON. Dla każdego wiersza wejściowego generuje parę klucz-wartość, w której klucz pochodzi z `<key_expression>`, a wartość z `<value_expression>`. Te pary klucz-wartość są następnie łączone w jeden obiekt JSON.

Zobacz też: [JSON_ARRAY_AGG](../aggregate-json-array-agg)

## Składnia Analyze

```python
func.json_object_agg(<key_expression>, <value_expression>)
```

## Przykłady Analyze
Szczegóły znajdziesz w przykładzie SQL

## Składnia SQL

```sql
JSON_OBJECT_AGG(<key_expression>, <value_expression>)
```

| Parametr         | Opis                                                                                                                                                   |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| key_expression   | Określa klucz w obiekcie JSON. **Obsługiwane są tylko wyrażenia tekstowe**. Jeśli `key_expression` ma wartość NULL, para klucz-wartość jest pomijana.   |
| value_expression | Określa wartość w obiekcie JSON. Może to być dowolny obsługiwany typ danych. Jeśli `value_expression` ma wartość NULL, para klucz-wartość jest pomijana. |

## Typ zwracany

Obiekt JSON.

## Przykłady SQL

Ten przykład pokazuje, jak JSON_OBJECT_AGG może agregować różne typy danych — takie jak liczby dziesiętne, liczby całkowite, warianty JSON i tablice — do obiektów JSON, przy czym kluczem każdego obiektu JSON jest kolumna b:

```sql
CREATE TABLE d (
    a DECIMAL(10, 2), 
    b STRING, 
    c INT, 
    d VARIANT, 
    e ARRAY(STRING)
);

INSERT INTO d VALUES
    (20, 'abc', NULL, '{"k":"v"}', ['a','b']),
    (10, 'de', 100, 'null', []),
    (4.23, NULL, 200, '"uvw"', ['x','y']),
    (5.99, 'xyz', 300, '[1,2,3]', ['z']);

SELECT
    json_object_agg(b, a) AS json_a,
    json_object_agg(b, c) AS json_c,
    json_object_agg(b, d) AS json_d,
    json_object_agg(b, e) AS json_e
FROM
    d;

-[ RECORD 1 ]-----------------------------------
json_a: {"abc":20.0,"de":10.0,"xyz":5.99}
json_c: {"de":100,"xyz":300}
json_d: {"abc":{"k":"v"},"de":null,"xyz":[1,2,3]}
json_e: {"abc":["a","b"],"de":[],"xyz":["z"]}
```
