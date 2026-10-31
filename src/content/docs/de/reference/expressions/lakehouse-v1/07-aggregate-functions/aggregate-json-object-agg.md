---
title: JSON_OBJECT_AGG (Lakehouse v1)
description: JSON_OBJECT_AGG – wandelt Schlüssel-Wert-Paare in ein JSON-Objekt um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-json-object-agg.md
---

Wandelt Schlüssel-Wert-Paare in ein JSON-Objekt um. Für jede Zeile der Eingabe wird ein Schlüssel-Wert-Paar erzeugt, bei dem der Schlüssel aus `<key_expression>` und der Wert aus `<value_expression>` abgeleitet wird. Diese Schlüssel-Wert-Paare werden anschließend zu einem einzelnen JSON-Objekt zusammengeführt.

Siehe auch: [JSON_ARRAY_AGG](../aggregate-json-array-agg)

## Analyze-Syntax

```python
func.json_object_agg(<key_expression>, <value_expression>)
```

## Analyze-Beispiele
Details finden Sie im SQL-Beispiel.

## SQL-Syntax

```sql
JSON_OBJECT_AGG(<key_expression>, <value_expression>)
```

| Parameter        | Beschreibung                                                                                                                                           |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| key_expression   | Gibt den Schlüssel im JSON-Objekt an. Unterstützt **nur Zeichenfolgenausdrücke**. Wenn `key_expression` den Wert NULL ergibt, wird das Schlüssel-Wert-Paar übersprungen.  |
| value_expression | Gibt den Wert im JSON-Objekt an. Kann ein beliebiger unterstützter Datentyp sein. Wenn `value_expression` den Wert NULL ergibt, wird das Schlüssel-Wert-Paar übersprungen. |

## Rückgabetyp

JSON-Objekt.

## SQL-Beispiele

Dieses Beispiel zeigt, wie JSON_OBJECT_AGG verschiedene Datentypen – etwa Dezimalzahlen, Ganzzahlen, JSON-Varianten und Arrays – zu JSON-Objekten aggregiert, wobei die Spalte b als Schlüssel jedes JSON-Objekts dient:

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
