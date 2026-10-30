---
title: JSON_TYPEOF (Lakehouse v1)
description: JSON_TYPEOF — retorna o tipo do nível principal de uma estrutura JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-typeof.md
---

Retorna o tipo do nível principal de uma estrutura JSON.

## Sintaxe do Analyze

```python
func.json_typeof(<json_string>)
```

## Exemplos do Analyze

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

## Sintaxe SQL

```sql
JSON_TYPEOF(<json_string>)
```

## Tipo de retorno

O tipo de retorno da função json_typeof (ou similar) é uma string que indica o tipo de dados do valor JSON interpretado. Os valores de retorno possíveis são: 'null', 'boolean', 'string', 'number', 'array' e 'object'.

## Exemplos de SQL

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
