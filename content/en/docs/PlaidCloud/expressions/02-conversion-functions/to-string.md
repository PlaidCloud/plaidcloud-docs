---
title: TO_STRING
---

Converts a value to String data type, or converts a Date value to a specific string format. To customize the format of date and time in PlaidCloud Lakehouse, you can utilize specifiers. These specifiers allow you to define the desired format for date and time values. For a comprehensive list of supported specifiers, see [Formatting Date and Time](../../00-sql-reference/10-data-types/20-data-type-time-date-types.md#formatting-date-and-time).

## SQL Syntax

```sql
TO_STRING( '<expr>' )

TO_STRING( '<date>', '<format>' )
```

## Aliases

- [DATE_FORMAT](../05-datetime-functions/date-format.md)
- [JSON_TO_STRING](../10-semi-structured-functions/json-to-string.md)
- [TO_TEXT](../02-conversion-functions/to-text.md)
- [TO_VARCHAR](to-varchar.md)

## Return Type

String.

## SQL Examples

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