---
title: JSON_TYPEOF
---

Returns the type of the main-level of a JSON structure.

## Analyze Syntax

```python
func.json_typeof(<json_string>)
```

## Analyze Example

```python
func.json_typeof(func.parse_json('null'))|
-----------------------------------------+
null                                     |

--
func.json_typeof(func.parse_json('true'))|
-----------------------------------------+
boolean                                  |

--
func.json_typeof(func.parse_json('"plaidcloud"'))|
-----------------------------------------------+
string                                         |

--
func.json_typeof(func.parse_json('-1.23'))|
------------------------------------------+
number                                    |

--
func.json_typeof(func.parse_json('[1,2,3]'))|
--------------------------------------------+
array                                       |

--
func.json_typeof(func.parse_json('{"name": "alice", "age": 30}'))|
-----------------------------------------------------------------+
object                                                           |
```

## SQL Syntax

```sql
JSON_TYPEOF(<json_string>)
```

## Return Type

The return type of the json_typeof function (or similar) is a string that indicates the data type of the parsed JSON value. The possible return values are: 'null', 'boolean', 'string', 'number', 'array', and 'object'.

## SQL Examples

```sql
-- Parsing a JSON value that is NULL
SELECT JSON_TYPEOF(PARSE_JSON(NULL));

--
func.json_typeof(func.parse_json(null))|
-----------------------------+
                             |

-- Parsing a JSON value that is the string 'null'
SELECT JSON_TYPEOF(PARSE_JSON('null'));

--
func.json_typeof(func.parse_json('null'))|
-------------------------------+
null                           |

SELECT JSON_TYPEOF(PARSE_JSON('true'));

--
func.json_typeof(func.parse_json('true'))|
-------------------------------+
boolean                        |

SELECT JSON_TYPEOF(PARSE_JSON('"PlaidCloud Lakehouse"'));

--
func.json_typeof(func.parse_json('"databend"'))|
-------------------------------------+
string                               |


SELECT JSON_TYPEOF(PARSE_JSON('-1.23'));

--
func.json_typeof(func.parse_json('-1.23'))|
--------------------------------+
number                          |

SELECT JSON_TYPEOF(PARSE_JSON('[1,2,3]'));

--
func.json_typeof(func.parse_json('[1,2,3]'))|
----------------------------------+
array                             |

SELECT JSON_TYPEOF(PARSE_JSON('{"name": "Alice", "age": 30}'));

--
func.json_typeof(func.parse_json('{"name": "alice", "age": 30}'))|
-------------------------------------------------------+
object                                                 |
```