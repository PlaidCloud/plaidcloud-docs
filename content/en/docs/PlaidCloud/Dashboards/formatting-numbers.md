---
title: Formatting Numbers and Other Data Types
slug: dashboard-formatting-numbers
weight: 3.0
description: How to format numbers and other data types to look how you want
date: 2023-12-18T06:49:48
---


## Formatting numbers and other data types

There are 2 ways of formatting numbers in PlaidCloud. One way is to transform the values in the tables directly, and a second (more common way) is to format them on display so the values don't lose precision in the table and the user can see the values in a cleaner, more appropriate way.

When I display a value on a dashboard, how do I format it the way I want?
The core way to display a value is through a chart object on a dashboard. Charts can be Tables, Big Numbers, Bar Charts, and so on. Each chart object may have a slightly different place or means to display the values. For example, in Tables, you can change the format for each column, and for a Big Number, you can change the format of the number.

To change the format, edit the chart and locate the `D3 FORMAT` or `NUMBER FORMAT` field. For a Big Number chart, click on the `CUSTOMIZE` tab, and you will see `NUMBER FORMAT`. For a Table, click on the `CUSTOMIZE` tab, select a number column (displayed with a #) in `CUSTOMIZE COLUMN` and you will see the `D3 FORMAT` field.

The default value is `Adaptive formatting`. This will adjust the format based on the values. But if you want to fix it to a format (i.e. $12.23 or 12,345,678), then you select the format you want from the dropdown or manually type a different value (if the field allows).

## D3 Formatting - what is it?

D3 Formatting is a structured, formalized means to display data results in a particular format. For example, in certain situations you may wish to display a large value as 3B (3 billion), formatted as `.3s` in D3 format, or as 3,001,238,383, formatted as `,d`. Another common example is the decision to represent dollar values with 2 decimal precision, or to round that to the nearest dollar ($,d) or $,.2f to show dollar sign, commas, 2 decimal precision, and a fixed point notation.
For a deeper dive into D3, see the following site: [GitHub D3](https://github.com/d3/d3-format)


## General D3 Format

The general structure of D3 is the following:

`[​[fill]align][sign][symbol][0][width][,][.precision][~][type]`

The fill can be any character (like a period, x or anything else). If you have a fill character, you then have an `align` character following it, which must be one of the following:

`>` - Right-aligned within the available space. (Default behavior).
`<` - Left-aligned within the available space.
`^` - Centered within the available space.
`=` - like >, but with any sign and symbol to the left of any padding.

The `sign` can be:
`-` - blank for zero or positive and a minus sign for negative. (Default behavior.)
`+` - a plus sign for zero or positive and a minus sign for negative.
`(` - nothing for zero or positive and parentheses for negative.
(space) - a space for zero or positive and a minus sign for negative.

The `symbol` can be:
`$` - apply currency symbol.
`#` - for binary, octal, or hexadecimal notation, prefix by 0b, 0o, or 0x, respectively.

The `zero` (0) option enables zero-padding; this implicitly sets fill to 0 and align to =.

The `width` defines the minimum field width; if not specified, then the width will be determined by the content. For example, if you have 8, the width of the field will be 8 characters.

The `comma` (,) option enables the use commas as separators (i.e. for thousands).

Depending on the type, the `precision` can either indicate the number of digits that follow the decimal point (types f and %), or the number of significant digits (types ​, e, g, r, s and p). If the precision is not specified, it defaults to 6 for all types except (none), which defaults to 12. Precision is ignored for integer formats (types b, o, d, x, and X) and character data (type c).

The `tilde` ~ option trims insignificant trailing zeros across all format types. This is most commonly used in conjunction with types r, e, s and %.

`types`
|Type |   Description                                                                               |
|-----|---------------------------------------------------------------------------------------------|
|e    |exponent notation                                                                            |
|f    |fixed point notation.
|g    |either decimal or exponent notation, rounded to significant digits.
|r    |decimal notation, rounded to significant digits.
|s    |decimal notation with an SI prefix, rounded to significant digits.
|%    |multiply by 100, and then decimal notation with a percent sign.
|p    |multiply by 100, round to significant digits, and then decimal notation with a percent sign.
|b    |binary notation, rounded to integer.
|o    |octal notation, rounded to integer.
|d    |decimal notation, rounded to integer.
|x    |hexadecimal notation, using lower-case letters, rounded to integer.
|X    |hexadecimal notation, using upper-case letters, rounded to integer.
|c    |character data, for a string of text.

## Examples
|Expression|Input|Output|Notes|
|----------|-----|------|-----|
|,d|12345.67|12,346|rounds the value to the nearest integer, adds commas
|$,.2f|12345.67|$12,345.67|Adds a $ symbol, has commas, 2 digits after the decimal
|$,d|12345.67|$12,346|
|.>10,|151925|...151,925|have periods to the left of the value, 10 characters wide, with commas
|,.2%|13.215|1,321.50%|have commas, 2 digits to the right of a decimal, convert to percentage, and show a % symbol
|x^+$16,.2f|123456|xx+$123,456.00xx| buffer with "x", centered, have a +/- symbol, $ symbol, 16 characters wide, have commas, 2 digit decimal
 