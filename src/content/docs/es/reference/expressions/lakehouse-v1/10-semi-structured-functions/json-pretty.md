---
title: JSON_PRETTY (Lakehouse v1)
description: JSON_PRETTY — da formato a los datos JSON para que sean más legibles y presentables.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-pretty.md
---

Da formato a los datos JSON para que sean más legibles y presentables. Agrega automáticamente sangría, saltos de línea y otros elementos de formato a los datos JSON para mejorar su representación visual.

## Sintaxis de Analyze

```python
func.json_pretty(<json_string>)
```

## Ejemplos de Analyze

```python
func.json_pretty(func.parse_json('{"person": {"name": "bob", "age": 25}, "location": "city"}'))

┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.json_pretty(func.parse_json('{"person": {"name": "bob", "age": 25}, "location": "city"}')) │
│                                         String                                                  │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ {                                                                                               │
│   "location": "City",                                                                           │
│   "person": {                                                                                   │
│     "age": 25,                                                                                  │
│     "name": "Bob"                                                                               │
│   }                                                                                             │
│ }                                                                                               │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
JSON_PRETTY(<json_string>)
```

## Tipo de retorno

String.

## Ejemplos de SQL

```sql
SELECT JSON_PRETTY(PARSE_JSON('{"name":"Alice","age":30}'));

---
┌──────────────────────────────────────────────────────┐
│ json_pretty(parse_json('{"name":"alice","age":30}')) │
│                        String                        │
├──────────────────────────────────────────────────────┤
│ {                                                    │
│   "age": 30,                                         │
│   "name": "Alice"                                    │
│ }                                                    │
└──────────────────────────────────────────────────────┘

SELECT JSON_PRETTY(PARSE_JSON('{"person": {"name": "Bob", "age": 25}, "location": "City"}'));

---
┌───────────────────────────────────────────────────────────────────────────────────────┐
│ json_pretty(parse_json('{"person": {"name": "bob", "age": 25}, "location": "city"}')) │
│                                         String                                        │
├───────────────────────────────────────────────────────────────────────────────────────┤
│ {                                                                                     │
│   "location": "City",                                                                 │
│   "person": {                                                                         │
│     "age": 25,                                                                        │
│     "name": "Bob"                                                                     │
│   }                                                                                   │
│ }                                                                                     │
└───────────────────────────────────────────────────────────────────────────────────────┘
```
