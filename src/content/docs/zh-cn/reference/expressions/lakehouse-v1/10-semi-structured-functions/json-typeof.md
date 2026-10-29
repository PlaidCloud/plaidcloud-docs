---
title: JSON_TYPEOF（Lakehouse v1）
description: JSON_TYPEOF — 返回 JSON 结构最外层的类型。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-typeof.md
---

返回 JSON 结构最外层的类型。

## Analyze 语法

```python
func.json_typeof(<json_string>)
```

## Analyze 示例

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

## SQL 语法

```sql
JSON_TYPEOF(<json_string>)
```

## 返回类型

json_typeof 函数（或类似函数）的返回类型是字符串，表示解析后 JSON 值的数据类型。可能的返回值为：'null'、'boolean'、'string'、'number'、'array' 和 'object'。

## SQL 示例

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
