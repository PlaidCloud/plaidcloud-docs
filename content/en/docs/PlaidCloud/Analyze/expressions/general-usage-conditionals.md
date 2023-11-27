---
title: General Usage Conditionals
slug: general-usage-conditionals
weight: 1.0
description: Simple If-then-else/case Operation, Complex Condition with Multiple Options, Coalesce
date: 2022-01-25T07:39:53
---


Below are conditionals, which allow for if/then/else functionality.


## The `case` operation

A "case" operation refers to a switch or a conditional control structure that allows the program to evaluate an expression and perform different actions based on the value of that expression. It can consist of multiple cases or conditions, each associated with a specific block of code to execute when the condition is met.

### Examples
#### A simple example
This example returns a person's name. It starts off searching to see if the first name column has a value (the "if"). If there is a value, concatenate the first name with the last name and return it (the "then"). If there isn't a first name, then return the last name only (the "else").

```python
case(
        (table.first_name.isnot(None), func.concat(table.first_name, table.last_name)), 
        else_ = table.last_name
    )
```


#### A more complex example with multiple conditions
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



## `Coalesce`

The coalesce function allows you to find the first non-null value in a set of columns.

This example finds the price set for the sale by looking in three possible fields and then returns the price times the number sold.

```python
func.coalesce(table_beta.adjusted_price, table_alpha.override_price, table_alpha.price) * table_beta.quantity_sold
```

Coalesce also works for text values.

This example will use the nickname if it is not null, or it will return the first name if there is no nickname. 

```python
func.coalesce(table.nickname, table.first_name)
```
