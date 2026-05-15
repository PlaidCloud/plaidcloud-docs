---
title: Lakehouse v1 Expressions
description: Lakehouse v1 expressions based on Databend SQL functions with SQLAlchemy references using func. prefixes.
sidebar:
  label: Lakehouse v1
---

Lakehouse v1 is built on the [Databend](https://databend.com/) SQL engine. For each function below, this site provides PlaidCloud-flavored syntax and examples; for the canonical upstream reference (with all edge cases and argument variants), see the **[Databend SQL function reference](https://docs.databend.com/sql/sql-functions/)**.

## Scalar Functions

- [Array Functions](./00-array-functions) — Perform array operations
- [Bitwise Expression Functions](./01-bitmap-functions) — Perform bitwise operations and manipulations
- [Conditional Expression Functions](./03-conditional-functions) — Implement conditional logic and case statements
- [Context Functions](./15-context-functions) — Provide information about the current SQL execution context
- [Conversion Functions](./02-conversion-functions) — Convert data types and cast values
- [Date & Time Functions](./05-datetime-functions) — Manipulate and format dates and times
- [Geospatial Functions](./09-geo-functions) — Handle and manipulate geospatial data
- [Geometry Functions](./09-geometry-functions) — Handle and manipulate geospatial geometry data
- [Interval Functions](./05-interval-functions) — Create and manipulate time intervals
- [Map Functions](./10-map-functions) — Create and manipulate map data structures
- [Numeric Functions](./04-numeric-functions) — Perform calculations and numeric operations
- [Search Functions](./10-search-functions) — Find values using expressions
- [Semi-structured and Structured Data Functions](./10-semi-structured-functions) — Work with JSON and other structured data formats
- [String Functions](./06-string-functions) — Manipulate strings and perform regular expression operations

## Aggregate Functions

- [Aggregate Functions](./07-aggregate-functions) — Calculate summaries like sum, average, count, etc.
- [Window Functions](./08-window-functions) — Provide aggregate calculations over a specified range of rows

## AI Functions

- [AI Functions](./11-ai-functions) — Leverage AI and machine learning capabilities

## Specialized Functions

- [Hash Functions](./12-hash-functions) — Generate hash values for data security and comparison
- [IP Address Functions](./14-ip-address-functions) — Manipulate and analyze IP address data
- [UUID Functions](./13-uuid-functions) — Generate and manipulate UUIDs

## System and Table Functions

- [Sequence Functions](./18-sequence-functions) — Generate sequential values
- [System Functions](./16-system-functions) — Access system-level information and perform control operations
- [Table Functions](./17-table-functions) — Return results in a tabular format

## Other Functions

- [Dictionary Functions](./19-dictionary-functions) — Work with dictionary data structures
- [Other Miscellaneous Functions](./20-other-functions) — A collection of various other functions
- [Test Functions](./19-test-functions) — Functions used for testing purposes
