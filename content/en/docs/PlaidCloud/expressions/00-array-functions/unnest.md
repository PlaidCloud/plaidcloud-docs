---
title: UNNEST
---

Unnests the array and returns the set of elements.

## Analyze Syntax

```python
func.unnest( <array> )
```

## Analyze Examples

```python
func.unnest([1, 2])

┌──────────────────────┐
│  func.unnest([1, 2]) │
├──────────────────────┤
│                    1 │
│                    2 │
└──────────────────────┘
```

## SQL Syntax

```sql
UNNEST( <array> )
```

## SQL Examples

```sql
SELECT UNNEST([1, 2]);

┌─────────────────┐
│  unnest([1, 2]) │
├─────────────────┤
│               1 │
│               2 │
└─────────────────┘

-- UNNEST(array) can be used as a table function.
SELECT * FROM UNNEST([1, 2]);

┌─────────────────┐
│      value      │
├─────────────────┤
│               1 │
│               2 │
└─────────────────┘
```

## A Practical Example
In the examples below, we will use the following table called contacts with the phones column defined with an array of text.

```python
CREATE TABLE contacts (
  id SERIAL PRIMARY KEY, 
  name VARCHAR (100), 
  phones TEXT []
);
```

The phones column is a one-dimensional array that holds various phone numbers that a contact may have.

To define multiple dimensional array, you add the square brackets.

For example, you can define a two-dimensional array as follows:

```python
column_name data_type [][]
```

An example of inserting data into that table
```python
INSERT INTO contacts (name, phones)
VALUES('John Doe',ARRAY [ '(408)-589-5846','(408)-589-5555' ]);
```
or
```python
INSERT INTO contacts (name, phones)
VALUES('Lily Bush','{"(408)-589-5841"}'),
      ('William Gate','{"(408)-589-5842","(408)-589-5843"}');
```

The unnest() function expands an array to a list of rows. For example, the following query expands all phone numbers of the phones array.

```python
SELECT 
  name, 
  unnest(phones) 
FROM 
  contacts;
```

Output:
|     name     |     unnest     |
|--------------|----------------|
| John Doe     | (408)-589-5846 |
| John Doe     | (408)-589-5555 |
| Lily Bush    | (408)-589-5841 |
| William Gate | (408)-589-5843 |
