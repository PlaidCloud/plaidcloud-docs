---
title: CASE
---

Handles IF/THEN logic. It is structured with at least one pair of `WHEN` and `THEN` statements. Every `CASE` statement must be concluded with the `END` keyword. The `ELSE` statement is optional, providing a way to capture values not explicitly specified in the `WHEN` and `THEN` statements.

## Analyze Examples

### A simple example
This example returns a person's name. It starts off searching to see if the first name column has a value (the "if"). If there is a value, concatenate the first name with the last name and return it (the "then"). If there isn't a first name, then return the last name only (the "else").

```python
case(
    (table.first_name.is_not(None), func.concat(table.first_name, table.last_name)), 
    else_ = table.last_name
)
```

### A more complex example with multiple conditions
This example returns a price based on quantity. "If" the quantity in the order is more than 100, then give the customer the special price. If it doesn't satisfy the first condition, go to the second. If the quantity is greater than 10 (11-100), then give the customer the bulk price. Otherwise give the customer the regular price.

```python
case( 
    (order_table.qty > 100, item_table.specialprice), 
    (order_table.qty > 10, item_table.bulkprice) , 
    else_=item_table.regularprice
)
```

This example returns the first initial of the person's first name. If the user's name is wendy, return W. Otherwise if the user's name is jack, return J. Otherwise return E.

```python
case( 
    (users_table.name == "wendy", "W"), 
    (users_table.name == "jack", "J"), 
    else_='E'
)
```

The above may also be written in shorthand as:

```python
case(
    {"wendy": "W", "jack": "J"}, 
    value=users_table.name, 
    else_='E' 
)
```

### Other Examples
In this example is from a Table:Lookup step where we are updating the "dock_final" column when the table1.dock_final value is Null.
```python
case(
    (table1.dock_final == Null, table2.dock_final),
    else_ = table1.dock_final
)
```

This example is from a Table:Lookup step where we are updating the "Marketing Channel" column when "Marketing Channel" in table1 is not 'none' or the "Serial Number" contains a '_'.
```python
case(
    (get_column(table1, 'Marketing Channel') != 'none', get_column(table1, 'Marketing Channel')),
    (get_column(table1, 'Serial Number').contains('_'), get_column(table1, 'Marketing Channel')),
    (get_column(table2, 'Marketing Channel').is_not(Null), get_column(table2, 'Marketing Channel')), 
    else_ = 'none'
)
```

## SQL Syntax

```sql
CASE
    WHEN <condition_1> THEN <value_1>
  [ WHEN <condition_2> THEN <value_2> ]
  [ ... ]
  [ ELSE <value_n> ]
END AS <column_name>
```

## SQL Examples

This example categorizes employee salaries using a CASE statement, presenting details with a dynamically assigned column named "SalaryCategory":

```sql
-- Create a sample table
CREATE TABLE Employee (
    EmployeeID INT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Salary INT
);

-- Insert some sample data
INSERT INTO Employee VALUES (1, 'John', 'Doe', 50000);
INSERT INTO Employee VALUES (2, 'Jane', 'Smith', 60000);
INSERT INTO Employee VALUES (3, 'Bob', 'Johnson', 75000);
INSERT INTO Employee VALUES (4, 'Alice', 'Williams', 90000);

-- Add a new column 'SalaryCategory' using CASE statement
-- Categorize employees based on their salary
SELECT
    EmployeeID,
    FirstName,
    LastName,
    Salary,
    CASE
        WHEN Salary < 60000 THEN 'Low'
        WHEN Salary >= 60000 AND Salary < 80000 THEN 'Medium'
        WHEN Salary >= 80000 THEN 'High'
        ELSE 'Unknown'
    END AS SalaryCategory
FROM
    Employee;

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│    employeeid   │     firstname    │     lastname     │      salary     │ salarycategory │
├─────────────────┼──────────────────┼──────────────────┼─────────────────┼────────────────┤
│               1 │ John             │ Doe              │           50000 │ Low            │
│               2 │ Jane             │ Smith            │           60000 │ Medium         │
│               4 │ Alice            │ Williams         │           90000 │ High           │
│               3 │ Bob              │ Johnson          │           75000 │ Medium         │
└──────────────────────────────────────────────────────────────────────────────────────────┘
```