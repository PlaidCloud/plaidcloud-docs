---
title: "TO_STRING (Conversion, Lakehouse v1)"
description: TO_STRING — convierte un valor al tipo de datos String o convierte un valor Date a un formato de cadena específico.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-string.md
---

Convierte un valor al tipo de datos String o convierte un valor Date a un formato de cadena específico. Para personalizar el formato de fecha y hora en PlaidCloud Lakehouse, puede usar especificadores. Estos especificadores le permiten definir el formato deseado para los valores de fecha y hora. Para ver una lista completa de los especificadores admitidos, consulte Formatting Date and Time.

## Sintaxis de Analyze

```python
func.to_string( '<expr>' )
```

## Ejemplos de Analyze

```python
func.date_format('1.23'), func.to_string('1.23'), func.to_text('1.23'), func.to_varchar('1.23'), func.json_to_string('1.23')

┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.date_format('1.23') │ func.to_string('1.23') │ func.to_text('1.23') │ func.to_varchar('1.23') │ func.json_to_string('1.23') │
├──────────────────────────┼────────────────────────┼──────────────────────┼─────────────────────────┼─────────────────────────────┤
│ 1.23                     │ 1.23                   │ 1.23                 │ 1.23                    │ 1.23                        │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘ 
```

## Sintaxis de SQL

```sql
TO_STRING( '<expr>' )

TO_STRING( '<date>', '<format>' )
```

## Alias

- [DATE_FORMAT](../../05-datetime-functions/date-format)
- [JSON_TO_STRING](../../10-semi-structured-functions/json-to-string)
- [TO_TEXT](../to-text)
- [TO_VARCHAR](../to-varchar)

## Tipo de retorno

String.

## Ejemplos de SQL

```sql
SELECT
  DATE_FORMAT('1.23'),
  TO_STRING('1.23'),
  TO_TEXT('1.23'),
  TO_VARCHAR('1.23'),
  JSON_TO_STRING('1.23');

┌─────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ date_format('1.23') │ to_string('1.23') │ to_text('1.23') │ to_varchar('1.23') │ json_to_string('1.23') │
├─────────────────────┼───────────────────┼─────────────────┼────────────────────┼────────────────────────┤
│ 1.23                │ 1.23              │ 1.23            │ 1.23               │ 1.23                   │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────┘

SELECT
  DATE_FORMAT('["Cooking", "Reading"]' :: JSON),
  TO_STRING('["Cooking", "Reading"]' :: JSON),
  TO_TEXT('["Cooking", "Reading"]' :: JSON),
  TO_VARCHAR('["Cooking", "Reading"]' :: JSON),
  JSON_TO_STRING('["Cooking", "Reading"]' :: JSON);

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ date_format('["cooking", "reading"]'::variant) │ to_string('["cooking", "reading"]'::variant) │ to_text('["cooking", "reading"]'::variant) │ to_varchar('["cooking", "reading"]'::variant) │ json_to_string('["cooking", "reading"]'::variant) │
├────────────────────────────────────────────────┼──────────────────────────────────────────────┼────────────────────────────────────────────┼───────────────────────────────────────────────┼───────────────────────────────────────────────────┤
│ ["Cooking","Reading"]                          │ ["Cooking","Reading"]                        │ ["Cooking","Reading"]                      │ ["Cooking","Reading"]                         │ ["Cooking","Reading"]                             │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

-- With one argument, the function converts input to a string without validating as a date.
SELECT
  DATE_FORMAT('20223-12-25'),
  TO_STRING('20223-12-25'),
  TO_TEXT('20223-12-25'),
  TO_VARCHAR('20223-12-25'),
  JSON_TO_STRING('20223-12-25');

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ date_format('20223-12-25') │ to_string('20223-12-25') │ to_text('20223-12-25') │ to_varchar('20223-12-25') │ json_to_string('20223-12-25') │
├────────────────────────────┼──────────────────────────┼────────────────────────┼───────────────────────────┼───────────────────────────────┤
│ 20223-12-25                │ 20223-12-25              │ 20223-12-25            │ 20223-12-25               │ 20223-12-25                   │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

SELECT
  DATE_FORMAT('2022-12-25', '%m/%d/%Y'),
  TO_STRING('2022-12-25', '%m/%d/%Y'),
  TO_TEXT('2022-12-25', '%m/%d/%Y'),
  TO_VARCHAR('2022-12-25', '%m/%d/%Y'),
  JSON_TO_STRING('2022-12-25', '%m/%d/%Y');

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ date_format('2022-12-25', '%m/%d/%y') │ to_string('2022-12-25', '%m/%d/%y') │ to_text('2022-12-25', '%m/%d/%y') │ to_varchar('2022-12-25', '%m/%d/%y') │ json_to_string('2022-12-25', '%m/%d/%y') │
├───────────────────────────────────────┼─────────────────────────────────────┼───────────────────────────────────┼──────────────────────────────────────┼──────────────────────────────────────────┤
│ 12/25/2022                            │ 12/25/2022                          │ 12/25/2022                        │ 12/25/2022                           │ 12/25/2022                               │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
