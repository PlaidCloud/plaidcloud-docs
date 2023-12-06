---
title: General Usage Mathematics Expressions
slug: general-usage-mathematics-expressions
weight: 5.0
description: Expression with Enhanced Transformation Capabilities
date: 2022-01-25T07:39:53
---

Expressions use Python [SQLAlchemy](https://www.sqlalchemy.org) syntax and provide powerful transformation capabilities.

{{< note >}}
Always use table.field references in expressions
{{< /note >}}

## Common Mathematics Expressions
| Analyze Expression | Operator | Description | Example | Result |
|--------------------|----------|-------------|---------|--------|
| + | + | addition | 2 + 3 | 5 |
| – | – | subtraction | 2 – 3 | -1 |
| * | * | multiplication | 2 * 3 | 6 |
| / | / | division (integer division truncates results) | 4 / 2 | 2 |
| column.op(‘%’) | % | modulo (remainder) | 5 % 4 | 1 |
| column.op(‘^’) | ^ | exponentiation | 2.0 ^ 3.0 | 8 |
| column.op(‘!’) | ! | factorial | 5 ! | 120 |
| column.op(‘!!’) | !! | factorial (prefix operator) | !! 5 | 120 |
| column.op(‘@’) | @ | absolute value | @ -5.0 | 5 |
| column.op(‘&’) | & | bitwise AND | 91 & 15 | 11 |
| column.op(‘#’) | ## | bitwise XOR | 17 ## 5 | 20 |
| column.op(‘~’) | ~ | bitwise NOT | ~1 | -2 |
| column.op(‘<<’) | << | bitwise shift left | 1 << 4 | 16 |
| column.op(‘>>’) | >> | bitwise shift right | 8 >> 2 | 2 |

## Mathematics Functions
| Analyze Expression | Return Type | Description | Example | Result |  |
|--------------------|-------------|-------------|---------|--------|--|
| func.abs(x) | (same as input) | absolute value | abs(-17.4 ) | 17.4 |  |
| func.cbrt(dp) | Big Float | cube root | cbrt(27.0 ) | 3 |  |
| func.ceil(dp or numeric) | (same as input) | smallest integer not less than argument | ceil(-42. 8) | -42 |  |
| func.ceiling(dp or numeric) | (same as input) | smallest integer not less than argument (alias for ceil) | ceiling(- 95.3) | -95 |  |
| func.degrees(dp) | Big Float | radians to degrees | degrees(0 .5) | 28.64788 97565412 |  |
| func.exp(dp or numeric) | (same as input) | exponential | exp(1.0) | 2.718281 82845905 |  |
| func.floor(dp or numeric) | (same as input) | largest integer not greater than argument | floor(-42 .8) | -43 |  |
| func.ln(dp or numeric) | (same as input) | natural logarithm | ln(2.0) | 0.693147 18055994 5 |  |
| func.log(dp or numeric) | (same as input) | base 10 logarithm | log(100.0 ) | 2 |  |
| func.log(b numeric, x numeric) | numeric | logarithm to base b | log(2.0, 64.0) | 6 |  |
| func.mod(y, x) | (same as argument types) | remainder of y/x | mod(9,4) | 1 |  |
| func.pi() | Big Float | “π” constant | pi() | 3.141592 65358979 |  |
| func.power(a dp, b dp) | Big Float | a raised to the power of b | power(9.0 , 3.0) | 729 |  |
| func.power(a numeric, b numeric) | numeric | a raised to the power of b | power(9.0 , 3.0) | 729 |  |
| func.radians(dp) | Big Float | degrees to radians | radians(4 5.0) | 0.785398 16339744 8 |  |
| func.random() | Big Float | random value in the range 0.0 <= x < 1.0 | random() |  |  |
| func.round(dp or numeric) | (same as input) | round to nearest integer | round(42. 4) | 42 |  |
| func.round(v numeric, s int) | numeric | round to s decimal places | round(42. 4382, 2) | 42.44 |  |
| func.setseed(dp) | integer | set seed for subsequent random() calls (value between 0 and 1.0) | setseed(0 .54823) | 11773149 59 |  |
| func.sign(dp or numeric) | (same as input) | sign of the argument (-1, 0, +1) | sign(-8.4 ) | -1 |  |
| func.sqrt(dp or numeric) | (same as input) | square root | sqrt(2.0) | 1.414213 5623731 |  |
| func.trunc(dp or numeric) | (same as input) | truncate toward zero | trunc(42. 8) | 42 |  |
| func.trunc(v numeric, s int) | numeric | truncate to s decimal places | trunc(42. 4382, 2) | 42.43 |  |
| func.width_bucket( op numeric, b1 numeric, b2 numeric, count int) | integer | return the bucket to which operand would be assigned in an equidepth histogram with count buckets, in the range b1 to b2 | width_bu cket(5.35 , 0.024, 10.06, 5) | 3 |  |
| func.least(value…) | (same as input) | Select the smallest value from a list. NULL values in the list are ignored. The result will be NULL only if all values are NULL. |  |  |  |
| func.greatest(value …) | (same as input) | Select the largest value from a list. NULL values in the list are ignored. The result will be NULL only if all values are NULL. |  |  |  |

## Trigonometric Functions
| Analyze Expression | Description |
|--------------------|-------------|
| func.acos(x) | inverse cosine |
| func.asin(x) | inverse sine |
| func.atan(x) | inverse tangent |
| func.atan2(x,y) | inverse tangent of x/y |
| func.cos(x) | cosine |
| func.cot(x) | cotangent |
| func.sin(x) | sine |
| func.tan(x) | tangent |
