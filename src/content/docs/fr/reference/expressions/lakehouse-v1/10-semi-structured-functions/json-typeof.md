---
title: JSON_TYPEOF (Lakehouse v1)
description: JSON_TYPEOF — renvoie le type du niveau principal d'une structure JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-typeof.md
---

Renvoie le type du niveau principal d'une structure JSON.

## Syntaxe Analyze

```python
func.json_typeof(<json_string>)
```

## Exemples Analyze

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

## Syntaxe SQL

```sql
JSON_TYPEOF(<json_string>)
```

## Type de retour

Le type de retour de la fonction json_typeof (ou équivalente) est une chaîne qui indique le type de données de la valeur JSON analysée. Les valeurs de retour possibles sont : 'null', 'boolean', 'string', 'number', 'array' et 'object'.

## Exemples SQL

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
