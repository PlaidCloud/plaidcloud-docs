---
title: TO_DATE
---

Converts an expression to a date, including:

- **Converting a timestamp-format string to a date**: Extracts a date from the given string.

- **Converting an integer to a date**: Interprets the integer as the number of days before (for negative numbers) or after (for positive numbers) the Unix epoch (midnight on January 1, 1970). Please note that a Date value ranges from `1000-01-01` to `9999-12-31`. PlaidCloud Lakehouse would return an error if you run "SELECT TO_DATE(9999999999999999999)".

- **Converting a string to a date using the specified format**: The function takes two arguments, converting the first string to a date based on the format specified in the second string. To customize the date and time format in PlaidCloud Lakehouse, specifiers can be used. For a comprehensive list of supported specifiers, see Formatting Date and Time.

Date formats are expressed using the `strftime` specification.  A quick reference is [here](https://devhints.io/strftime).

See also: [TO_TIMESTAMP](../to-timestamp)

## strftime Parameters

### Quick Reference

#### Date

| Example         | Output                 |
| ---             | ---                    |
| `%m/%d/%Y`      | `06/05/2013`           |
| `%A, %B %e, %Y` | `Sunday, June 5, 2013` |
| `%b %e %a`      | `Jun 5 Sun`            |

#### Time

| Example         | Output                 |
| ---             | ---                    |
| `%H:%M`         | `23:05`                |
| `%I:%M %p`      | `11:05 PM`             |


### Date

| Symbol | Example                  | Area        |
| ---    | ---                      | ---         |
| `%a`   | `Sun`                    | **Weekday** |
| `%A`   | `Sunday`                 |             |
| `%w`   | `0`..`6` _(Sunday is 0)_ |             |
| ---    | ---                      | ---         |
| `%y`   | `13`                     | **Year**    |
| `%Y`   | `2013`                   |             |
| ---    | ---                      | ---         |
| `%b`   | `Jan`                    | **Month**   |
| `%B`   | `January`                |             |
| `%m`   | `01`..`12`               |             |
| ---    | ---                      | ---         |
| `%d`   | `01`..`31`               | **Day**     |
| `%e`   | `1`..`31`                |             |


### Time

| Symbol | Example      | Area                |
| ---    | ---          | ---                 |
| `%l`   | `1`          | Hour                |
| `%H`   | `00`..`23`   | 24h Hour            |
| `%I`   | `01`..`12`   | 12h Hour            |
| --     | ---          | ---                 |
| `%M`   | `00`..`59`   | Minute              |
| `%S`   | `00`..`60`   | Second              |
| ---    | ---          | ---                 |
| `%p`   | `AM`         | AM or PM            |
| `%Z`   | `+08`        | Time zone           |
| ---    | ---          | ---                 |
| `%j`   | `001`..`366` | Day of the year     |
| `%%`   | `%`          | Literal % character |


## Analyze Syntax

```python
func.to_date('<timestamp_expr>')
func.to_date(<integer>)
func.to_date('<string>', '<format>')
```

## Analyze Examples

```python
func.typeof(func.to_date('2022-01-02')), func.typeof(func.str_to_date('2022-01-02'))

┌───────────────────────────────────────────────────────────────────────────────────────┐
│ func.typeof(func.to_date('2022-01-02')) │ func.typeof(func.str_to_date('2022-01-02')) │
├─────────────────────────────────────────┼─────────────────────────────────────────────┤
│ DATE                                    │ DATE                                        │
└───────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
-- Convert a timestamp-format string
TO_DATE('<timestamp_expr>')

-- Convert an integer
TO_DATE(<integer>)

-- Convert a string using the given format
TO_DATE('<string>', '<format>')
```

## Aliases

- [DATE](../date)
- [STR_TO_DATE](../str-to-date)

## Return Type

The function returns a date in the format "YYYY-MM-DD":

```sql
SELECT TYPEOF(TO_DATE('2022-01-02')), TYPEOF(STR_TO_DATE('2022-01-02'));

┌───────────────────────────────────────────────────────────────────┐
│ typeof(to_date('2022-01-02')) │ typeof(str_to_date('2022-01-02')) │
├───────────────────────────────┼───────────────────────────────────┤
│ DATE                          │ DATE                              │
└───────────────────────────────────────────────────────────────────┘
```

To convert the returned date back to a string, use the [DATE_FORMAT](../date-format) function:

```sql
SELECT DATE_FORMAT(TO_DATE('2022-01-02')) AS dt, TYPEOF(dt);

┌─────────────────────────┐
│     dt     │ typeof(dt) │
├────────────┼────────────┤
│ 2022-01-02 │ VARCHAR    │
└─────────────────────────┘
```

## SQL Examples

### SQL Examples 1: Converting a Timestamp-Format String

```sql
SELECT TO_DATE('2022-01-02T01:12:00+07:00'), STR_TO_DATE('2022-01-02T01:12:00+07:00');

┌─────────────────────────────────────────────────────────────────────────────────┐
│ to_date('2022-01-02t01:12:00+07:00') │ str_to_date('2022-01-02t01:12:00+07:00') │
├──────────────────────────────────────┼──────────────────────────────────────────┤
│ 2022-01-01                           │ 2022-01-01                               │
└─────────────────────────────────────────────────────────────────────────────────┘

SELECT TO_DATE('2022-01-02'), STR_TO_DATE('2022-01-02');

┌───────────────────────────────────────────────────┐
│ to_date('2022-01-02') │ str_to_date('2022-01-02') │
├───────────────────────┼───────────────────────────┤
│ 2022-01-02            │ 2022-01-02                │
└───────────────────────────────────────────────────┘
```

### SQL Examples 2: Converting an Integer

```sql
SELECT TO_DATE(1), STR_TO_DATE(1), TO_DATE(-1), STR_TO_DATE(-1);

┌───────────────────────────────────────────────────────────────────┐
│ to_date(1) │ str_to_date(1) │ to_date((- 1)) │ str_to_date((- 1)) │
│    Date    │      Date      │      Date      │        Date        │
├────────────┼────────────────┼────────────────┼────────────────────┤
│ 1970-01-02 │ 1970-01-02     │ 1969-12-31     │ 1969-12-31         │
└───────────────────────────────────────────────────────────────────┘
```

### SQL Examples 3: Converting a String using the Given Format

```sql
SELECT TO_DATE('12/25/2022','%m/%d/%Y'), STR_TO_DATE('12/25/2022','%m/%d/%Y');

┌───────────────────────────────────────────────────────────────────────────┐
│ to_date('12/25/2022', '%m/%d/%y') │ str_to_date('12/25/2022', '%m/%d/%y') │
├───────────────────────────────────┼───────────────────────────────────────┤
│ 2022-12-25                        │ 2022-12-25                            │
└───────────────────────────────────────────────────────────────────────────┘
```