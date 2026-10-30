---
title: JSON_TYPEOF (Lakehouse v1)
description: JSON_TYPEOF — Gibt den Typ der obersten Ebene einer JSON-Struktur zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-typeof.md
---

Gibt den Typ der obersten Ebene einer JSON-Struktur zurück.

## Analyze Syntax

```python
func.json_typeof(<json_string>)
```

## Analyze Examples

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

Der Rückgabetyp der Funktion json_typeof (oder einer ähnlichen Funktion) ist eine Zeichenfolge, die den Datentyp des geparsten JSON-Werts angibt. Mögliche Rückgabewerte sind: 'null', 'boolean', 'string', 'number', 'array' und 'object'.

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
